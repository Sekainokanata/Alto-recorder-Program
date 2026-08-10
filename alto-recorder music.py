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
	MELODY_TUNETA,
	MELODY_CHORUS,
	ENABLE_MELODY,
 	ENABLE_MELODY_TUNETA,
	ENABLE_MELODY_CHORUS,
	ENABLE_BASS,
	ENABLE_DRUMS,
	ENABLE_GUITAR,
)
from alto_recorder_program.sequencer import build_sequence_events, mix_tracks, render_track, write_wav
from alto_recorder_program.synth import (
    render_bass_note, render_drum_hit, render_electric_guitar_brush,
    render_electric_guitar_note, render_recorder_note, render_recorder_note_husky,
)

def build_song() -> None:
	source_path = SCRIPT_DIR / "Alto recorder.wav"
	output_dir = SCRIPT_DIR / "output"

	source_clip = extract_reference_clip(str(source_path), start_sec=6.0, end_sec=11.0)
	print(f"Reference clip: {source_clip.estimated_note} ({source_clip.estimated_f0:.2f} Hz)")

	melody_items = MELODY if ENABLE_MELODY else []
	melody_tuneta_items = MELODY_TUNETA if ENABLE_MELODY_TUNETA else []
	melody_chorus_items = MELODY_CHORUS if ENABLE_MELODY_CHORUS else []
	bass_items = BASS if ENABLE_BASS else []
	drum_items = DRUMS if ENABLE_DRUMS else []
	guitar_items = GUITAR if ENABLE_GUITAR else []

	melody_events = build_sequence_events(melody_items)
	melody_tuneta_events = build_sequence_events(melody_tuneta_items)
	melody_chorus_events = build_sequence_events(melody_chorus_items)
	bass_events = build_sequence_events(bass_items)
	drum_events = build_sequence_events(drum_items)
	guitar_events = build_sequence_events(guitar_items)

	def render_melody_event(event):
		val = event.value
		if isinstance(val, (list, tuple)):
			parts = [
				render_recorder_note(
					source_clip, note, event.duration, BPM,
					velocity=event.velocity,
					ornament=event.ornament,
					ornament_semitones=event.ornament_semitones,
					ornament_ms=event.ornament_ms,
				)
				for note in val
			]
			return sum(parts) if parts else np.zeros(0, dtype=np.float32)
		else:
			return render_recorder_note(
				source_clip, val, event.duration, BPM,
				velocity=event.velocity,
				ornament=event.ornament,
				ornament_semitones=event.ornament_semitones,
				ornament_ms=event.ornament_ms,
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
 
 
	def render_melody_tuneta_event(event):
		val = event.value
		if isinstance(val, (list, tuple)):
			parts = [
				render_recorder_note_husky(
					source_clip, note, event.duration, BPM,
					velocity=event.velocity,
					ornament=event.ornament,
					ornament_semitones=event.ornament_semitones,
					ornament_ms=event.ornament_ms,
				)
				for note in val
			]
			return sum(parts) if parts else np.zeros(0, dtype=np.float32)
		else:
			return render_recorder_note_husky(
					source_clip, val, event.duration, BPM,
					velocity=event.velocity,
					ornament=event.ornament,
					ornament_semitones=event.ornament_semitones,
					ornament_ms=event.ornament_ms,
			)

	melody_tuneta_track = render_track(
		melody_tuneta_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_melody_tuneta_event(event),
	)
	def render_melody_chorus_event(event):
		val = event.value
		
		def render_both(note_str):
			if str(note_str).strip().lower() == "mute":
				return np.zeros(0, dtype=np.float32)
			
			# 通常の音とハスキーな音を両方生成
			note_normal = render_recorder_note(source_clip, note_str, event.duration, BPM, velocity=event.velocity)
			note_husky = render_recorder_note_husky(source_clip, note_str, event.duration, BPM, velocity=event.velocity)
			
			# 2つの波形を合成 (シーケンサーのmix_tracks関数を利用)
			return mix_tracks([note_normal, note_husky])

		if isinstance(val, (list, tuple)):
			parts = [render_both(note) for note in val]
			return mix_tracks(parts) if parts else np.zeros(0, dtype=np.float32)
		else:
			return render_both(val)

	melody_chorus_track = render_track(
		melody_chorus_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_melody_chorus_event(event),
	)
	

	def render_drum_event(event):
		val = event.value
		def render_single_hit(hit_name):
			if str(hit_name).strip().lower() == "mute":
				return np.zeros(0, dtype=np.float32)
			else:
				return render_drum_hit(
					source_clip,  # ← リコーダー音声を渡す
					hit_name,
					event.duration,
					BPM,
					source_clip.sample_rate,
					velocity=event.velocity,
				)

		# リストまたはタプルの場合は和音（同時打ち）として処理
		if isinstance(val, (list, tuple)):
			parts = [render_single_hit(h) for h in val]
			mix = mix_tracks(parts) if parts else np.zeros(0, dtype=np.float32)
			return mix
		else:
			return render_single_hit(val)

	drum_track = render_track(
		drum_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_drum_event(event), # ← 上で作った関数を呼び出す
	)

	guitar_ir_path = SCRIPT_DIR / GUITAR_IR_FILE

	def render_guitar_event(event):
		val = event.value
		
		# 単音またはブラッシング音を処理する内部関数
		def render_single_note(note_str):
			if str(note_str).strip().upper() == "X":
				return render_electric_guitar_brush(
					source_clip.sample_rate,
					guitar_ir_path,
					velocity=event.velocity,
				)
			elif str(note_str).strip().lower() == "mute":
				return np.zeros(0, dtype=np.float32)
			else:
				return render_electric_guitar_note(
					source_clip,
					note_str,
					event.duration,
					BPM,
					guitar_ir_path,
					velocity=event.velocity,
				)

		# valがリストかタプルなら和音として処理
		if isinstance(val, (list, tuple)):
			parts = [render_single_note(note) for note in val]
			mix = sum(parts) if parts else np.zeros(0, dtype=np.float32)
			return mix
		else:
			return render_single_note(val)

	guitar_track = render_track(
		guitar_events,
		BPM,
		source_clip.sample_rate,
		lambda event: render_guitar_event(event),
	)

	final_mix = mix_tracks([melody_track, melody_tuneta_track, melody_chorus_track, bass_track, drum_track, guitar_track])

	write_wav(output_dir / "melody.wav", melody_track, source_clip.sample_rate)
	write_wav(output_dir / "melody_tuneta.wav", melody_tuneta_track, source_clip.sample_rate)
	write_wav(output_dir / "melody_chorus.wav", melody_chorus_track, source_clip.sample_rate)
	write_wav(output_dir / "bass.wav", bass_track, source_clip.sample_rate)
	write_wav(output_dir / "drums.wav", drum_track, source_clip.sample_rate)
	write_wav(output_dir / "guitar.wav", guitar_track, source_clip.sample_rate)
	write_wav(output_dir / "final_mix.wav", final_mix, source_clip.sample_rate)

	print(f"Exported stems and final mix to: {output_dir}")


if __name__ == "__main__":
	build_song()
