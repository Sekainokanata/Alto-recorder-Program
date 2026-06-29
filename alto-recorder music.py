from __future__ import annotations

from pathlib import Path
import sys
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
	sys.path.insert(0, str(SCRIPT_DIR))

from alto_recorder_program.analysis import extract_reference_clip
from alto_recorder_program.score import (
	BASS,
	BPM,
	DRUMS,
	GUITAR,
	GUITAR_IR_FILE,
	MELODY,
	ENABLE_MELODY,
	ENABLE_BASS,
	ENABLE_DRUMS,
	ENABLE_GUITAR,
)
from alto_recorder_program.sequencer import build_sequence_events, mix_tracks, render_track, write_wav
from alto_recorder_program.synth import render_bass_note, render_drum_hit, render_electric_guitar_brush, render_electric_guitar_note, render_recorder_note


def build_song() -> None:
	source_path = SCRIPT_DIR / "Alto recorder.wav"
	output_dir = SCRIPT_DIR / "output"

	source_clip = extract_reference_clip(str(source_path), start_sec=6.0, end_sec=11.0)
	print(f"Reference clip: {source_clip.estimated_note} ({source_clip.estimated_f0:.2f} Hz)")

	melody_items = MELODY if ENABLE_MELODY else []
	bass_items = BASS if ENABLE_BASS else []
	drum_items = DRUMS if ENABLE_DRUMS else []
	guitar_items = GUITAR if ENABLE_GUITAR else []

	melody_events = build_sequence_events(melody_items)
	bass_events = build_sequence_events(bass_items)
	drum_events = build_sequence_events(drum_items)
	guitar_events = build_sequence_events(guitar_items)

	def render_melody_event(event):
		val = event.value
		if isinstance(val, (list, tuple)):
			parts = [
				render_recorder_note(source_clip, note, event.duration, BPM, velocity=event.velocity)
				for note in val
			]
			mix = sum(parts) if parts else np.zeros(0, dtype=np.float32)
			return mix
		else:
			return render_recorder_note(
				source_clip,
				val,
				event.duration,
				BPM,
				velocity=event.velocity,
			)

	melody_track = render_track(
		melody_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_melody_event(event),
	)

	bass_track = render_track(
		bass_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_bass_note(
			event.value,
			event.duration,
			BPM,
			source_clip.sample_rate,
			velocity=event.velocity,
		),
	)

	drum_track = render_track(
		drum_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_drum_hit(
			event.value,
			event.duration,
			BPM,
			source_clip.sample_rate,
			velocity=event.velocity,
		),
	)

	guitar_ir_path = SCRIPT_DIR / GUITAR_IR_FILE
	guitar_track = render_track(
		guitar_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_electric_guitar_brush(
			source_clip.sample_rate,
			guitar_ir_path,
			velocity=event.velocity,
		)
		if str(event.value).strip().upper() == "X"
		else render_electric_guitar_note(
			source_clip,
			event.value,
			event.duration,
			BPM,
			guitar_ir_path,
			velocity=event.velocity,
		),
	)

	final_mix = mix_tracks([melody_track, bass_track, drum_track, guitar_track])

	write_wav(output_dir / "melody.wav", melody_track, source_clip.sample_rate)
	write_wav(output_dir / "bass.wav", bass_track, source_clip.sample_rate)
	write_wav(output_dir / "drums.wav", drum_track, source_clip.sample_rate)
	write_wav(output_dir / "guitar.wav", guitar_track, source_clip.sample_rate)
	write_wav(output_dir / "final_mix.wav", final_mix, source_clip.sample_rate)

	print(f"Exported stems and final mix to: {output_dir}")


if __name__ == "__main__":
	build_song()
