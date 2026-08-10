from __future__ import annotations

from .instrument.velocity import (
    MELODY_TUNETA_BASE_VELOCITY,
    MELODY_BASE_VELOCITY,
    MELODY_CHORUS_BASE_VELOCITY,
    BASS_BASE_VELOCITY,
    GUITAR_BASE_VELOCITY,
    DRUM_BASE_VELOCITY,
)
from .instrument.melody import MELODY
from .instrument.melody_tuneta import MELODY_TUNETA
from .instrument.melody_chorus import MELODY_CHORUS
from .instrument.bass import BASS
from .instrument.guitar import GUITAR
from .instrument.drums import DRUMS

BPM = 190.0
TIME_SIGNATURE = (4, 4)

# Track enable flags: set False to mute a track temporarily.
ENABLE_MELODY = True
ENABLE_MELODY_TUNETA = True
ENABLE_MELODY_CHORUS = True


ENABLE_BASS = True
ENABLE_DRUMS = True
ENABLE_GUITAR = True


# Electric guitar IR file used by convolution.
# Change only this file name/path to swap cabinet tone.
GUITAR_IR_FILE = "57_grill_edge_pres_4.wav"

# Melody, bass, guitar and drums are written as sequential note lists,
# split out per part under alto_recorder_program/instrument/.
# Start positions are generated automatically in the sequencer.
