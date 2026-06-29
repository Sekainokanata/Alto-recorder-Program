from __future__ import annotations

import math
import re

NOTE_BASES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_BASES_FLAT = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
NOTE_TO_SEMITONE = {
    "C": 0,
    "B#": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "Fb": 4,
    "E#": 5,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
    "Cb": 11,
}
NOTE_RE = re.compile(r"^([A-Ga-g])([#b♯♭]?)(-?\d+)$")

# Japanese solfège to letter mapping (ド= C, レ= D, ミ= E, ファ= F, ソ= G, ラ= A, シ= B)
JAPANESE_TO_LETTER = {
    "ド": "C",
    "レ": "D",
    "ミ": "E",
    "ファ": "F",
    "ソ": "G",
    "ラ": "A",
    "シ": "B",
}

# Map full-width digits to ASCII digits for inputs like 'ド３'
FULLWIDTH_DIGITS = str.maketrans("０１２３４５６７８９", "0123456789")


def note_to_midi(note: str) -> int:
    text = note.strip()

    # Try A-G style first
    match = NOTE_RE.match(text)
    if match:
        letter, accidental, octave_text = match.groups()
        base = letter.upper() + accidental.replace("♯", "#").replace("♭", "b")
        if base not in NOTE_TO_SEMITONE:
            raise ValueError(f"Unsupported note spelling: {note}")
        octave = int(octave_text)
        return 12 * (octave + 1) + NOTE_TO_SEMITONE[base]

    # Try Japanese solfège like 'ド3', 'ファ♯4', possibly with full-width digits
    # Normalize full-width digits
    text_norm = text.translate(FULLWIDTH_DIGITS)
    # Regex for Japanese names (ファ is two chars) and optional accidental and octave
    jap_re = re.compile(r"^(ド|レ|ミ|ファ|ソ|ラ|シ)([#b♯♭]?)(-?\d+)$")
    jap_match = jap_re.match(text_norm)
    if jap_match:
        syl, accidental, octave_text = jap_match.groups()
        letter = JAPANESE_TO_LETTER.get(syl)
        if letter is None:
            raise ValueError(f"Unsupported Japanese note name: {syl}")
        base = letter + accidental.replace("♯", "#").replace("♭", "b")
        if base not in NOTE_TO_SEMITONE:
            raise ValueError(f"Unsupported note spelling: {note}")
        octave = int(octave_text)
        return 12 * (octave + 1) + NOTE_TO_SEMITONE[base]

    raise ValueError(f"Invalid note name: {note}")


def midi_to_note(midi: int, prefer_flats: bool = False) -> str:
    octave = midi // 12 - 1
    pitch_class = midi % 12
    name = NOTE_BASES_FLAT[pitch_class] if prefer_flats else NOTE_BASES_SHARP[pitch_class]
    return f"{name}{octave}"


def note_to_frequency(note: str, a4_hz: float = 440.0) -> float:
    midi = note_to_midi(note)
    return a4_hz * (2.0 ** ((midi - 69) / 12.0))


def duration_to_beats(duration) -> float:
    if isinstance(duration, (int, float)):
        return float(duration)

    text = str(duration).strip()
    dotted = text.endswith(".")
    if dotted:
        text = text[:-1]

    if "/" in text:
        numerator_text, denominator_text = text.split("/", 1)
        beats = 4.0 * float(numerator_text) / float(denominator_text)
    else:
        beats = float(text)

    if dotted:
        beats *= 1.5
    return beats


def beats_to_seconds(beats: float, bpm: float) -> float:
    return (60.0 / bpm) * beats


def seconds_to_beats(seconds: float, bpm: float) -> float:
    return seconds / (60.0 / bpm)
