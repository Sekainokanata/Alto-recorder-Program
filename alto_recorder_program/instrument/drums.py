from __future__ import annotations

from .velocity import DRUM_BASE_VELOCITY

DRUMS = [
    #書き方例{"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    #tam2がlower
    # LUV ME LUV ME
    {"value": ["kick-bass", "crash-cymbal"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    # 間奏
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": ["kick-bass", "crash-cymbal"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    # 間奏
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "tam-h", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},

    # 間奏
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "tam-h", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["tam-h", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["tam-h", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["tam-h", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 間奏
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # 間奏
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value":  "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},

    # 愛憎愛憎
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 渦巻いて
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 大東京狂騒
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 歌って
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 廻れ廻
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # れ時代の
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 生き恥に
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # ずぶ濡れで
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},

    # 愛憎愛憎
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # を喰らって
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 参ろう大層
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # な様で
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 離れ離
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # れで終いよ
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 然らば又
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # 逢いましょう
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},

    # 間奏
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},


    # ド
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "crash-cymbal", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    # ラマチックに
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # 溺れて 未完
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # 成な私を
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # 認めて 気休
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # めのフィク
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # ション 嘘と
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # 真の不協和
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
    # 音 出来損
    {"value": "Mute", "duration": "1/1", "velocity": DRUM_BASE_VELOCITY},
    
    # な愛でも
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 許して 構わ
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["hi-hat", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # ない 此の舞台
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 生き抜いて 咬ま
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["hi-hat", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["hi-hat", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # せ狗のハイテン
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # ション ヤラレっ
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["hi-hat", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # ぱなしじゃ 大人し
    {"value": ["kick-bass", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "tam-f"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},

    
    # くはなれない
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},

    # LUV ME LUV ME
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 正しさばかりで
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 全部奪って
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 愛憎塗れで
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # KILL ME KILL ME
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 此処を連れ出して
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # え～
    {"value": "Mute", "duration": "1/1", "velocity": DRUM_BASE_VELOCITY},


    # 間奏
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "tam-f", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    {"value": "snare", "duration": "1/16", "velocity": DRUM_BASE_VELOCITY},
    
    

    # 愛憎愛憎
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 抱き合って
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 最高潮よ
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 何時だって
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 騙し騙
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # しで良いの
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 代償なんて
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # 気にしないよ
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},

    # 愛憎愛憎
    {"value": ["kick-bass", "hi-hat"], "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    # に足宛いて
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 外交愛想
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 振り撒いて
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 万物問答
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 無用で終いよ
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 然らば又
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    
    # 逢いましょう
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["kick-bass", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": ["snare", "hi-hat"], "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},
    {"value": "hi-hat", "duration": "1/8", "velocity": DRUM_BASE_VELOCITY},

    # 間奏
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "kick-bass", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": DRUM_BASE_VELOCITY},
    
    {"value": "crash-cymbal", "duration": "5/4", "velocity": DRUM_BASE_VELOCITY},
    
]
