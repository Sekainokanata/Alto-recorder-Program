"""Audio arrangement toolkit for Alto recorder projects."""

from .analysis import extract_reference_clip
from .notes import duration_to_beats, beats_to_seconds, note_to_frequency, note_to_midi
from .sequencer import Event, build_sequence_events, render_track, mix_tracks, write_wav
from .synth import (
    render_bass_note,
    render_drum_hit,
    render_recorder_note,
)
