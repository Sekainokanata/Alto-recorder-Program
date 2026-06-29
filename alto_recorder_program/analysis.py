from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import librosa
import soundfile as sf

from .notes import midi_to_note


@dataclass(frozen=True)
class SourceClip:
    samples: np.ndarray
    sample_rate: int
    start_sec: float
    end_sec: float
    estimated_f0: float
    estimated_midi: float
    estimated_note: str


def load_mono_audio(filepath: str) -> tuple[np.ndarray, int]:
    samples, sample_rate = sf.read(filepath, always_2d=False)
    samples = np.asarray(samples, dtype=np.float32)
    if samples.ndim > 1:
        samples = samples[:, 0]
    return samples, sample_rate


def extract_segment(samples: np.ndarray, sample_rate: int, start_sec: float, end_sec: float) -> np.ndarray:
    start_index = max(0, int(round(start_sec * sample_rate)))
    end_index = min(len(samples), int(round(end_sec * sample_rate)))
    if start_index >= end_index:
        raise ValueError("The requested segment is empty.")
    return samples[start_index:end_index]


def estimate_fundamental(samples: np.ndarray, sample_rate: int) -> float:
    clipped = np.asarray(samples, dtype=np.float32)
    if clipped.size == 0:
        raise ValueError("Cannot estimate pitch from an empty signal.")

    clipped = librosa.util.normalize(clipped)

    try:
        f0_series = librosa.yin(clipped, fmin=40.0, fmax=1500.0, sr=sample_rate)
        valid = f0_series[np.isfinite(f0_series) & (f0_series > 0)]
        if valid.size:
            return float(np.median(valid))
    except Exception:
        pass

    spectrum = np.fft.rfft(clipped)
    magnitudes = np.abs(spectrum)
    frequencies = np.fft.rfftfreq(clipped.size, d=1.0 / sample_rate)
    peak_index = int(np.argmax(magnitudes[1:]) + 1)
    return float(frequencies[peak_index])


def extract_reference_clip(filepath: str, start_sec: float = 6.0, end_sec: float = 11.0) -> SourceClip:
    samples, sample_rate = load_mono_audio(filepath)
    segment = extract_segment(samples, sample_rate, start_sec, end_sec)
    estimated_f0 = estimate_fundamental(segment, sample_rate)
    estimated_midi = 69.0 + 12.0 * np.log2(estimated_f0 / 440.0)
    estimated_note = midi_to_note(int(round(estimated_midi)))

    return SourceClip(
        samples=segment,
        sample_rate=sample_rate,
        start_sec=start_sec,
        end_sec=end_sec,
        estimated_f0=estimated_f0,
        estimated_midi=estimated_midi,
        estimated_note=estimated_note,
    )
