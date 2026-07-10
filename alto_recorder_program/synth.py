from __future__ import annotations

from functools import lru_cache
import math
from pathlib import Path

import librosa
import numpy as np

try:
    from pedalboard import Convolution, Distortion, Pedalboard, Reverb, PitchShift
except Exception:
    Convolution = None
    Distortion = None
    Pedalboard = None
    Reverb = None
    PitchShift = None

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

###################################    
###################################    
###################################    
###################################    
###################################    

@lru_cache(maxsize=8)
def _build_guitar_board(ir_file: str):
    if Pedalboard is None:
        raise RuntimeError("pedalboard is required for electric guitar rendering. Install with: pip install pedalboard")
    return Pedalboard(
        [
            # ① ピッチシフト: オクターブ下にしてギターの太い帯域に合わせる
            PitchShift(semitones=-24),
            
            # ② ディストーション: ファズのような割れた歪み
            Distortion(drive_db=45.0),
            
            # ③ キャビネットシミュレータ(IR)
            Convolution(impulse_response_filename=ir_file, mix=1.0),
            
            # ④ リバーブ: 空間的な広がりを足して馴染ませる
            Reverb(room_size=0.1, damping=0.9, wet_level=0.15),
        ]
    )
    
###################################    
###################################    
###################################    
###################################    
###################################    


def render_electric_guitar_note(
    source_clip: SourceClip,
    target_note: str,
    duration,
    bpm: float,
    ir_file: str | Path,
    velocity: float = 1.0,
    octave_shift: int = 2,
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

KIND_GAIN = {
    "kick-bass": 2.0,  # ここを1.0〜2.0くらいで好みに調整
    "snare": 0.5,
    "hi-hat": 0.5,
}



def render_drum_hit(
    source_clip: SourceClip,
    kind: str, 
    duration, 
    bpm: float, 
    sample_rate: int, 
    velocity: float = 1.0
) -> np.ndarray:
    import scipy.signal  # フィルター処理用ライブラリを読み込み

    kind = kind.lower()
    
    # --- 1. 種類ごとのパラメータ設定 ---
    if kind == "kick-bass":
        n_steps = -60
        decay_sec = 0.4
        mix_noise = 0.0
        attack_noise = 0.02  # ★キックのノイズは極限まで減らす
    elif kind == "snare":
        n_steps = -12
        decay_sec = 0.25
        mix_noise = 0.7
        attack_noise = 0.5
    elif kind in {"hi-hat", "hat"}:
        n_steps = 24
        decay_sec = 0.08
        mix_noise = 0.9
        attack_noise = 0.8
    elif kind == "tam-h":
        n_steps = -17
        decay_sec = 0.4
        mix_noise = 0.0
        attack_noise = 0.4
    elif kind == "tam-l":
        n_steps = -24
        decay_sec = 0.45
        mix_noise = 0.0
        attack_noise = 0.4
    elif kind == "tam-f":
        n_steps = -40
        decay_sec = 0.5
        mix_noise = 0.0
        attack_noise = 0.4
    elif kind == "crash-cymbal":
        n_steps = 12
        decay_sec = 1.5
        mix_noise = 0.8
        attack_noise = 0.8
    else:
        raise ValueError(f"Unsupported drum kind: {kind}")

    # --- 2. 原音のピッチシフト ---
    shifted = librosa.effects.pitch_shift(
        source_clip.samples.astype(np.float32), 
        sr=source_clip.sample_rate, 
        n_steps=n_steps
    )

    # --- 3. フィルター処理（★ここが音色を劇的に分けるポイント） ---
    nyq = 0.5 * sample_rate  # ナイキスト周波数
    
    if kind == "kick-bass":
        # ローパスフィルター：250Hz以下の「重低音」だけを通し、シャリシャリ音を消す
        b, a = scipy.signal.butter(2, 250.0 / nyq, btype='low')
        shifted = scipy.signal.filtfilt(b, a, shifted)
        shifted *= 50.0 # 低音だけ残すと音量が下がるのでブーストする
        
    elif kind in {"hi-hat", "hat", "crash-cymbal"}:
        # ハイパスフィルター：2000Hz以上の「金属音」だけを通し、モコモコ感を消す
        b, a = scipy.signal.butter(2, 2000.0 / nyq, btype='high')
        shifted = scipy.signal.filtfilt(b, a, shifted)

    # --- 4. 長さとエンベロープの調整 ---
    target_len = max(1, int(round(decay_sec * sample_rate)))
    if len(shifted) > target_len:
        shifted = shifted[:target_len]
    else:
        shifted = np.pad(shifted, (0, target_len - len(shifted)))

    t = np.arange(target_len, dtype=np.float32) / sample_rate

    if kind == "crash-cymbal":
        body_env = np.exp(-t * 2.5)
    elif kind in {"hi-hat", "hat"}:
        body_env = np.exp(-t * 40.0)
    elif kind in {"tam-h", "tam-l", "tam-f"}:
        body_env = np.exp(-t * 10.0)
    elif kind == "kick-bass":
        body_env = np.exp(-t * 6.0) # キックは余韻を少し長めに
    else:
        body_env = np.exp(-t * 15.0)

    attack_env = np.exp(-t * 80.0)

    # --- 5. 音の合成 ---
    noise = RNG.normal(0.0, 1.0, size=target_len).astype(np.float32)
    
    # ノイズ側にもフィルターをかける（ハイハットのノイズから低音を抜く）
    if kind in {"hi-hat", "hat", "crash-cymbal", "snare"}:
        b, a = scipy.signal.butter(2, 1000.0 / nyq, btype='high')
        noise = scipy.signal.filtfilt(b, a, noise)

    body_signal = shifted * body_env * (1.0 - mix_noise)
    body_noise_signal = noise * body_env * mix_noise
    attack_signal = noise * attack_env * attack_noise

    # タムのみに原音（高音）の打撃感を足す（キックバスからは削除して純粋な低音にする）
    if kind in {"tam-h", "tam-l", "tam-f"}:
        raw_source = source_clip.samples.astype(np.float32)
        if len(raw_source) > target_len:
            raw_source = raw_source[:target_len]
        else:
            raw_source = np.pad(raw_source, (0, target_len - len(raw_source)))
            
        pitch_drop_env = np.exp(-t * 50.0)
        attack_signal += raw_source * pitch_drop_env * 0.4

    signal = body_signal + body_noise_signal + attack_signal

    # スピーカーへの負荷（クリックノイズ）防止用の極短フェードイン
    attack_len = min(target_len, int(0.001 * sample_rate))
    if attack_len > 0:
        signal[:attack_len] *= np.linspace(0.0, 1.0, attack_len, dtype=np.float32)
        
    out = normalize_audio(signal) * float(velocity)
    out *= KIND_GAIN.get(kind, 1.0)
    return out


def render_recorder_note_husky(
    source_clip: SourceClip,
    target_note: str,
    duration,
    bpm: float,
    velocity: float = 1.0,
    octave_shift: int = 0,
    breath_amount: float = 0.2,   # 息ノイズの混合量（0〜0.3くらいが自然）
    grit_drive_db: float = 10.0,   # 歪みの強さ(dB)。上げるほどガラつく
) -> np.ndarray:
    import scipy.signal  # ブレスノイズの帯域整形用

    target_beats = duration_to_beats(duration)
    target_seconds = beats_to_seconds(target_beats, bpm)

    source_midi = float(source_clip.estimated_midi)
    target_midi = float(note_to_midi(target_note) + octave_shift * 12)
    n_steps = target_midi - source_midi

    # --- ①〜③: MELODYと同じ土台処理 ---
    shifted = librosa.effects.pitch_shift(
        source_clip.samples.astype(np.float32), sr=source_clip.sample_rate, n_steps=n_steps
    )
    stretched = fit_duration(shifted, source_clip.sample_rate, target_seconds)
    shaped = apply_fade(stretched, source_clip.sample_rate)

    sr = source_clip.sample_rate

    # --- ④ 息成分(ブレスノイズ)を音量エンベロープに沿って混ぜる ---
    noise = RNG.normal(0.0, 1.0, size=len(shaped)).astype(np.float32)
    nyq = 0.5 * sr
    b, a = scipy.signal.butter(2, [2000.0 / nyq, 7000.0 / nyq], btype="band")
    breath_noise = scipy.signal.filtfilt(b, a, noise).astype(np.float32)

    envelope = np.abs(shaped)
    if envelope.size:
        win = max(1, int(sr * 0.01))
        kernel = np.ones(win, dtype=np.float32) / win
        envelope = np.convolve(envelope, kernel, mode="same")

    husky = shaped + breath_noise * envelope * breath_amount

    # --- ⑤ ごく軽い歪みでガラつき(ラスプ感)を追加 ---
    if Pedalboard is not None and Distortion is not None:
        board = Pedalboard([Distortion(drive_db=grit_drive_db)])
        husky = board(husky[np.newaxis, :], sr)[0]

    return normalize_audio(husky) * float(velocity)


#breath_amountを上げる → 「囁くような」息多めの声
# grit_drive_dbを上げる → 「がなり」「潰れ気味」なガラガラ声
# 両方低めにすると単に少しハスキー、両方高めだとかなりダミ声寄りになります