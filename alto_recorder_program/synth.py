from __future__ import annotations

from functools import lru_cache
import math
from pathlib import Path

import librosa
import numpy as np

try:
    from pedalboard import Convolution, Distortion, Pedalboard, Reverb
except Exception:
    Convolution = None
    Distortion = None
    Pedalboard = None
    Reverb = None

from .analysis import SourceClip
from .notes import beats_to_seconds, duration_to_beats, note_to_frequency, note_to_midi

RNG = np.random.default_rng(12345)


def normalize_audio(samples: np.ndarray, peak: float = 0.95) -> np.ndarray:
    samples = np.asarray(samples, dtype=np.float32)
    max_abs = float(np.max(np.abs(samples))) if samples.size else 0.0
    if max_abs <= 0.0:
        return samples
    return np.clip(samples / max_abs * peak, -1.0, 1.0)


def apply_fade(samples: np.ndarray, sample_rate: int, attack_ms: float = 5.0, release_ms: float = 20.0) -> np.ndarray:
    samples = np.asarray(samples, dtype=np.float32)
    if samples.size == 0:
        return samples

    attack_len = min(len(samples), max(1, int(sample_rate * attack_ms / 1000.0)))
    release_len = min(len(samples), max(1, int(sample_rate * release_ms / 1000.0)))

    envelope = np.ones(len(samples), dtype=np.float32)
    envelope[:attack_len] *= np.linspace(0.0, 1.0, attack_len, dtype=np.float32)
    envelope[-release_len:] *= np.linspace(1.0, 0.0, release_len, dtype=np.float32)
    return samples * envelope


def fit_duration(samples: np.ndarray, sample_rate: int, target_seconds: float) -> np.ndarray:
    samples = np.asarray(samples, dtype=np.float32)
    if target_seconds <= 0.0:
        return np.zeros(0, dtype=np.float32)
    if samples.size == 0:
        return np.zeros(int(round(target_seconds * sample_rate)), dtype=np.float32)

    current_seconds = len(samples) / sample_rate
    adjusted = samples
    if current_seconds > 0.0:
        rate = current_seconds / target_seconds
        if abs(rate - 1.0) > 0.01:
            try:
                adjusted = librosa.effects.time_stretch(adjusted, rate=rate)
            except Exception:
                pass

    target_len = max(1, int(round(target_seconds * sample_rate)))
    if len(adjusted) > target_len:
        adjusted = adjusted[:target_len]
    elif len(adjusted) < target_len:
        adjusted = np.pad(adjusted, (0, target_len - len(adjusted)))
    return adjusted.astype(np.float32)


def render_recorder_note(source_clip: SourceClip, target_note: str, duration, bpm: float, velocity: float = 1.0, octave_shift: int = 0) -> np.ndarray:
    target_beats = duration_to_beats(duration)
    target_seconds = beats_to_seconds(target_beats, bpm)

    source_midi = float(source_clip.estimated_midi)
    target_midi = float(note_to_midi(target_note) + octave_shift * 12)
    n_steps = target_midi - source_midi

    shifted = librosa.effects.pitch_shift(source_clip.samples.astype(np.float32), sr=source_clip.sample_rate, n_steps=n_steps)
    stretched = fit_duration(shifted, source_clip.sample_rate, target_seconds)
    shaped = apply_fade(stretched, source_clip.sample_rate)
    return normalize_audio(shaped) * float(velocity)


@lru_cache(maxsize=8)
def _build_guitar_board(ir_file: str):
    if Pedalboard is None:
        raise RuntimeError("pedalboard is required for electric guitar rendering. Install with: pip install pedalboard")
    return Pedalboard(
        [
            Distortion(drive_db=42.0),
            Convolution(impulse_response_filename=ir_file, mix=1.0),
            Reverb(room_size=0.15, damping=0.8, wet_level=0.1),
        ]
    )


def render_electric_guitar_note(
    source_clip: SourceClip,
    target_note: str,
    duration,
    bpm: float,
    ir_file: str | Path,
    velocity: float = 1.0,
    octave_shift: int = -1,
) -> np.ndarray:
    ir_path = Path(ir_file)
    if not ir_path.exists():
        raise FileNotFoundError(f"Guitar IR file not found: {ir_path}")

    target_beats = duration_to_beats(duration)
    target_seconds = beats_to_seconds(target_beats, bpm)

    source_midi = float(source_clip.estimated_midi)
    target_midi = float(note_to_midi(target_note) + octave_shift * 12)
    n_steps = target_midi - source_midi

    shifted = librosa.effects.pitch_shift(source_clip.samples.astype(np.float32), sr=source_clip.sample_rate, n_steps=n_steps)
    stretched = fit_duration(shifted, source_clip.sample_rate, target_seconds)
    shaped = apply_fade(stretched, source_clip.sample_rate)

    board = _build_guitar_board(str(ir_path))
    effected = board(shaped[np.newaxis, :], source_clip.sample_rate)
    effected_mono = effected[0] if effected.ndim == 2 else effected
    return normalize_audio(effected_mono) * float(velocity)


def render_electric_guitar_brush(
    sample_rate: int,
    ir_file: str | Path,
    velocity: float = 1.0,
    brush_seconds: float = 0.08,
) -> np.ndarray:
    # Duration is intentionally fixed for brushing; score duration is ignored for value='X'.
    length = max(1, int(round(float(brush_seconds) * sample_rate)))
    noise = RNG.uniform(-1.0, 1.0, size=length).astype(np.float32)

    t = np.arange(length, dtype=np.float32) / float(sample_rate)
    envelope = np.exp(-t * 60.0).astype(np.float32)
    raw_brush = noise * envelope

    ir_path = Path(ir_file)
    if not ir_path.exists():
        raise FileNotFoundError(f"Guitar IR file not found: {ir_path}")

    board = _build_guitar_board(str(ir_path))
    effected = board(raw_brush[np.newaxis, :], sample_rate)
    effected_mono = effected[0] if effected.ndim == 2 else effected
    return normalize_audio(effected_mono) * float(velocity)


def render_bass_note(note: str, duration, bpm: float, sample_rate: int, velocity: float = 1.0) -> np.ndarray:
    beats = duration_to_beats(duration)
    seconds = beats_to_seconds(beats, bpm)
    length = max(1, int(round(seconds * sample_rate)))
    t = np.arange(length, dtype=np.float32) / sample_rate
    freq = note_to_frequency(note)

    body = 0.82 * np.sin(2.0 * math.pi * freq * t)
    body += 0.18 * np.sin(2.0 * math.pi * 2.0 * freq * t)
    body += 0.08 * np.sin(2.0 * math.pi * 0.5 * freq * t)

    attack = np.minimum(1.0, t / max(1e-6, seconds * 0.08))
    release = np.minimum(1.0, (seconds - t) / max(1e-6, seconds * 0.18))
    envelope = np.clip(np.minimum(attack, release), 0.0, 1.0)
    return normalize_audio(body * envelope) * float(velocity)


def render_drum_hit(kind: str, duration, bpm: float, sample_rate: int, velocity: float = 1.0) -> np.ndarray:
    beats = duration_to_beats(duration)
    seconds = beats_to_seconds(beats, bpm)
    length = max(1, int(round(seconds * sample_rate)))
    t = np.arange(length, dtype=np.float32) / sample_rate
    envelope = np.exp(-t * 18.0)

    if kind == "kick":
        freq = 140.0 * np.exp(-t * 10.0) + 44.0
        phase = 2.0 * math.pi * np.cumsum(freq) / sample_rate
        body = np.sin(phase)
        click = np.sin(2.0 * math.pi * 2500.0 * t) * np.exp(-t * 180.0)
        signal = 0.95 * body * envelope + 0.18 * click
    elif kind == "snare":
        noise = RNG.normal(0.0, 1.0, size=length).astype(np.float32)
        mid = np.sin(2.0 * math.pi * 180.0 * t) * np.exp(-t * 35.0)
        signal = 0.85 * noise * envelope + 0.15 * mid
    elif kind in {"hat", "hihat", "hi-hat"}:
        noise = RNG.normal(0.0, 1.0, size=length).astype(np.float32)
        high = noise - np.concatenate([[0.0], noise[:-1]])
        signal = high * np.exp(-t * 60.0)
    else:
        raise ValueError(f"Unsupported drum kind: {kind}")

    return normalize_audio(signal) * float(velocity)
