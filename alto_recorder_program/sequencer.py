# from __future__ import annotations

# from dataclasses import dataclass
# from pathlib import Path
# from typing import Callable, Iterable, Sequence

# import numpy as np
# import soundfile as sf

# from .notes import beats_to_seconds, duration_to_beats
# from .synth import normalize_audio


# @dataclass(frozen=True)
# class Event:
#     value: str
#     duration: object
#     start_beats: float | None = None
#     velocity: float = 1.0


# def build_sequence_events(items: Sequence[dict]) -> list[Event]:
#     events: list[Event] = []
#     cursor = 0.0
#     for item in items:
#         duration_beats = duration_to_beats(item["duration"])
#         start_beats = item.get("start_beats")
#         if start_beats is None:
#             start_beats = cursor
#             cursor = start_beats + duration_beats
#         events.append(
#             Event(
#                 value=item["value"],
#                 duration=item["duration"],
#                 start_beats=float(start_beats),
#                 velocity=float(item.get("velocity", 1.0)),
#             )
#         )
#     return events


# def event_end_beats(event: Event) -> float:
#     start = float(event.start_beats or 0.0)
#     return start + duration_to_beats(event.duration)


# def render_track(
#     events: Sequence[Event],
#     bpm: float,
#     sample_rate: int,
#     renderer: Callable[[Event], np.ndarray],
#     tail_seconds: float = 1.0,
# ) -> np.ndarray:
#     if not events:
#         return np.zeros(0, dtype=np.float32)

#     total_beats = max(event_end_beats(event) for event in events)
#     total_seconds = beats_to_seconds(total_beats, bpm) + tail_seconds
#     mix = np.zeros(max(1, int(round(total_seconds * sample_rate))), dtype=np.float32)

#     for event in events:
#         # Skip mute/rest events
#         if str(event.value).lower() == "mute":
#             continue
        
#         start_beats = float(event.start_beats or 0.0)
#         start_seconds = beats_to_seconds(start_beats, bpm)
#         start_index = int(round(start_seconds * sample_rate))
#         rendered = renderer(event)
#         end_index = min(len(mix), start_index + len(rendered))
#         if end_index <= start_index:
#             continue
#         mix[start_index:end_index] += rendered[: end_index - start_index]

#     return mix


# def mix_tracks(tracks: Sequence[np.ndarray]) -> np.ndarray:
#     if not tracks:
#         return np.zeros(0, dtype=np.float32)

#     max_length = max(len(track) for track in tracks)
#     mix = np.zeros(max_length, dtype=np.float32)
#     for track in tracks:
#         mix[: len(track)] += track
#     return mix


# def write_wav(path: str | Path, samples: np.ndarray, sample_rate: int) -> None:
#     path = Path(path)
#     path.parent.mkdir(parents=True, exist_ok=True)
#     sf.write(path, samples.astype(np.float32), sample_rate)


from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence
from concurrent.futures import ThreadPoolExecutor # ← 追加

import numpy as np
import soundfile as sf

from .notes import beats_to_seconds, duration_to_beats
from .synth import normalize_audio


@dataclass(frozen=True)
class Event:
    value: str
    duration: object
    start_beats: float | None = None
    velocity: float = 1.0
    ornament: str | None = None            # ← 追加
    ornament_semitones: float | None = None
    ornament_ms: float | None = None


def build_sequence_events(items: Sequence[dict]) -> list[Event]:
    events: list[Event] = []
    cursor = 0.0
    for item in items:
        duration_beats = duration_to_beats(item["duration"])
        start_beats = item.get("start_beats")
        if start_beats is None:
            start_beats = cursor
            cursor = start_beats + duration_beats
        events.append(
            Event(
                value=item["value"],
                duration=item["duration"],
                start_beats=float(start_beats),
                velocity=float(item.get("velocity", 1.0)),
                ornament=item.get("ornament"),                     # ← 追加
                ornament_semitones=item.get("ornament_semitones"),
                ornament_ms=item.get("ornament_ms"),
            )
        )
    return events


def event_end_beats(event: Event) -> float:
    # (変更なし)
    start = float(event.start_beats or 0.0)
    return start + duration_to_beats(event.duration)


def render_track(
    events: Sequence[Event],
    bpm: float,
    sample_rate: int,
    renderer: Callable[[Event], np.ndarray],
    tail_seconds: float = 1.0,
) -> np.ndarray:
    if not events:
        return np.zeros(0, dtype=np.float32)

    total_beats = max(event_end_beats(event) for event in events)
    total_seconds = beats_to_seconds(total_beats, bpm) + tail_seconds
    mix = np.zeros(max(1, int(round(total_seconds * sample_rate))), dtype=np.float32)

    # --- ここから変更 ---
    # 1つの音符を処理する関数を内部で定義
    def process_event(event: Event):
        if str(event.value).lower() == "mute":
            return None
        start_beats = float(event.start_beats or 0.0)
        start_seconds = beats_to_seconds(start_beats, bpm)
        start_index = int(round(start_seconds * sample_rate))
        rendered = renderer(event) # ここが一番重い音声合成処理
        return start_index, rendered

    # ThreadPoolExecutorを使って、全音符の処理を並列化して一気に走らせる
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_event, events)

    # 並列で生成された音を順番に合成する
    for res in results:
        if res is not None:
            start_index, rendered = res
            end_index = min(len(mix), start_index + len(rendered))
            if end_index > start_index:
                mix[start_index:end_index] += rendered[: end_index - start_index]
    # --- ここまで変更 ---

    return mix


def mix_tracks(tracks: Sequence[np.ndarray]) -> np.ndarray:
    # (変更なし)
    if not tracks:
        return np.zeros(0, dtype=np.float32)

    max_length = max(len(track) for track in tracks)
    mix = np.zeros(max_length, dtype=np.float32)
    for track in tracks:
        mix[: len(track)] += track
    return mix


def write_wav(path: str | Path, samples: np.ndarray, sample_rate: int) -> None:
    # (変更なし)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(path, samples.astype(np.float32), sample_rate)