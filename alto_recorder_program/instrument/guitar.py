from __future__ import annotations

from .velocity import GUITAR_BASE_VELOCITY

    ####参照：https://www.youtube.com/watch?v=l1EnnIRk0e4
GUITAR = [   
    # LUV ME LUV ME
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##4弦7
    {"value": "Mute", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #間奏
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5}, 
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},#3弦
    {"value": "D5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "F5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "D5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    
    {"value": "E5", "duration": "1/2", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ

    
    # HATE ME HATE ME
    {"value": "Mute", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    #間奏
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5}, 
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "C6", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY*1.5},
   
    {"value": "D6", "duration": "7/16", "velocity": GUITAR_BASE_VELOCITY*1.5},#1/16 + 1/8+ 1/4 = 7/16 (小節マタギ)
    
    # LUV ME LUV ME
    {"value": "C6", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #間奏
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "C6", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "G5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    
    {"value": "D5", "duration": "1/2", "velocity": GUITAR_BASE_VELOCITY*1.5},##小節マタギ
    
    
    # KILL ME KILL ME
    {"value": "Mute", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},


    
    #間奏
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},#３弦
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "G5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "B4", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "F#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "G#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    #間奏
    {"value": "A5", "duration": "1/4","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A3", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A4", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    
    # 愛憎愛憎
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    # 渦巻いて
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #大東京狂騒
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "F3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    #歌って
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #廻れ廻
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # れ時代の
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    #生き恥に
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},

    
    #ずぶ濡れで
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 愛憎愛憎
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    # を喰らって
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #参ろう大層
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "F3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    #な様で
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #離れ離
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # れで終いよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 然らば又
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    
    
    # 逢いましょう
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 間奏
    {"value": "A4", "duration": "6/4", "velocity": GUITAR_BASE_VELOCITY*0.3},##小節マタギ
    
    # ド
    
    {"value": "Mute", "duration": "1/2","velocity": GUITAR_BASE_VELOCITY},
    
    # ラマチックに
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # 溺れて 未完
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # 成な私を
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # 認めて 気休
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # めのフィク
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # ション 嘘と
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # 真の不協和
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # 音 出来損
    {"value": "Mute", "duration": "1/1","velocity": GUITAR_BASE_VELOCITY},
    
    # な愛でも
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 許して 構わ
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # ない 此の舞台
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 生き抜いて 咬ま
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # せ狗のハイテン
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},

    # ション ヤラレっ
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},

    # ぱなしじゃ 大人し
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},

    
    # くはなれない
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},

    
    # LUV ME LUV ME
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #正しさばかりで
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #全部奪って
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #愛憎塗れで
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #此処を連れ出して
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # え～
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "G5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "B4", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "F#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "G#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY*1.5},
    
    #間奏
    {"value": "A5", "duration": "1/4","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A3", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A4", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY*1.5},
    
    # 愛憎愛憎
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    # 抱き合って
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #最高潮よ
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "F3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    #何時だって
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #騙し騙
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # しで良いの
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    #代償なんて
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    
    #気にしないよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 愛憎愛憎
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    # に足宛いて
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #外交愛想
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "F3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    #振り撒いて
    {"value": "C4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B3", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #万物問答
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 無用で終いよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    # 然らば又
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},    
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    
    
    
    # 逢いましょう
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY*0.5},
    {"value": "A4", "duration": "5/4", "velocity": GUITAR_BASE_VELOCITY*0.5},
]
