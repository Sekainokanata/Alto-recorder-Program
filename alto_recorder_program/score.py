from __future__ import annotations

BPM = 190.0
TIME_SIGNATURE = (4, 4)

# Track enable flags: set False to mute a track temporarily.
ENABLE_MELODY = True
ENABLE_MELODY_TUNETA = True
ENABLE_MELODY_CHORUS = True


ENABLE_BASS = False
ENABLE_DRUMS = False
ENABLE_GUITAR = False



MELODY_TUNETA_BASE_VELOCITY = 0.3
MELODY_BASE_VELOCITY = 0.3
MELODY_CHORUS_BASE_VELOCITY = 0.3


BASS_BASE_VELOCITY = 0.4
GUITAR_BASE_VELOCITY = 0.1
DRUM_BASE_VELOCITY = 0.5

# Electric guitar IR file used by convolution.
# Change only this file name/path to swap cabinet tone.
GUITAR_IR_FILE = "57_grill_edge_pres_4.wav"

# Melody and bass are written as sequential note lists.
# Start positions are generated automatically in the sequencer.


####進捗1:MELODY と　BASS　は完成。GUITAR はまだ。DRUMS はまだ。　2024/06/10 19:00
MELODY = [
    # LUV ME LUV ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # HATE ME HATE ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # LUV ME LUV ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # KILL ME KILL ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    
    # 愛憎愛憎
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 渦巻いて
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    
    # 大東京狂騒
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 歌って
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 廻れ廻
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # れ時代の
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 生き恥に
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # ずぶ濡れで
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    
    # 愛憎愛憎
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # を喰らって
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 参ろう大層
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # な様で
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #離れ離
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #れで終いよ
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #然らば又
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #逢いましょう
    {"value": "ミ4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #ド
    {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #ラマチックに
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    
    #溺れて 未完
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #成な私を
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    
    #認めて 気休
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # #めのフィク
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ション 嘘と
    # {"value": "ラ3", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
   
    # #真の不協
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # #和音 出来損
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #な愛でも
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #許して 構わ
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #ない 此の舞台
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #生き抜いて 咬ま
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # #せ狗のハイテン
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ション ヤラレっ
    # {"value": "ラ3", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ぱなしじゃ　大人し
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #くはなれない
    # {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # LUV ME LUV ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #正しさばかりで
    {"value": "ラ4", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ5", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ド5", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # HATE ME HATE ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #全部奪って
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # LUV ME LUV ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #愛憎塗れで
    
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ5", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ5", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ド5", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # KILL ME KILL ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "6/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #此処を連れ出して
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #え～
    {"value": "ラ4", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    ##サビ～##
    
    # 愛憎愛憎
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 抱き合って
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 最高潮よ
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 何時だって
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 騙し騙
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # しで良いの
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 代償なんて
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # 気にしないよ
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    
    # 愛憎愛憎
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # に足宛いて
    {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 外交愛想
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # 振り撒いて
    {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #万物問答
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #無用で終いよ
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #然らば又
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #逢いましょう
    {"value": "ミ4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    #{"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    

]
MELODY_TUNETA = [    
    # LUV ME LUV ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # HATE ME HATE ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # LUV ME LUV ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # KILL ME KILL ME
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    # {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 渦巻いて
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 大東京狂騒
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 歌って
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 廻れ廻
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # れ時代の
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 生き恥に
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # ずぶ濡れで
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # を喰らって
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 参ろう大層
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # な様で
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #離れ離
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #れで終いよ
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #然らば又
    {"value": "ファ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #逢いましょう
    {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #ド
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ラマチックに
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # #溺れて 未完
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #成な私を
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # #認めて 気休
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "3/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # #めのフィク
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # #ション 嘘と
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},

   
    # #真の不協
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    
    # #和音 出来損
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ#3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    
    # #な愛でも
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #許して 構わ
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ない 此の舞台
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #生き抜いて 咬ま
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},

    # #せ狗のハイテン
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # #ション ヤラレっ
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # #ぱなしじゃ　大人し
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},

    
    # #くはなれない
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ#3", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8

    
    # LUV ME LUV ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #正しさばかりで
    {"value": "ラ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # HATE ME HATE ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #全部奪って
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ド4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # LUV ME LUV ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    #愛憎塗れで
    
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ミ4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    
    # KILL ME KILL ME
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "6/8","velocity": MELODY_BASE_VELOCITY},
    
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #此処を連れ出して
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ファ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #え～
    {"value": "ミ4", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    ##サビ～##
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 抱き合って
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 最高潮よ
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 何時だって
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},    
    # # 騙し騙
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # しで良いの
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 代償なんて
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 気にしないよ
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # に足宛いて
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 外交愛想
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 振り撒いて
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #万物問答
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #無用で終いよ
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #然らば又
    {"value": "ファ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ソ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    #逢いましょう
    {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    #{"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
]
MELODY_CHORUS = [
    # LUV ME LUV ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 渦巻いて
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 大東京狂騒
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 歌って
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 廻れ廻
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # れ時代の
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 生き恥に
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # ずぶ濡れで
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # を喰らって
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 参ろう大層
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # な様で
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #離れ離
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #れで終いよ
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #然らば又
    # {"value": "ファ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #逢いましょう
    # {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #ド
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ラマチックに
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # #溺れて 未完
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #成な私を
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # #認めて 気休
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "3/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # #めのフィク
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # #ション 嘘と
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},

   
    # # #真の不協
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # # #和音 出来損
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # # {"value": "Mute", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    # # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #な愛でも
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #許して 構わ
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #ない 此の舞台
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #生き抜いて 咬ま
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "5/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},

    # # #せ狗のハイテン
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # #ション ヤラレっ
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # #ぱなしじゃ　大人し
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},

    
    # # #くはなれない
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ#3", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},

    
    # LUV ME LUV ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #正しさばかりで
    # {"value": "ラ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #全部奪って
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    # {"value": "ド4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #愛憎塗れで
    
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    
    # {"value": "ミ4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},##小節マタギ
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY*1.5},
    {"value": ["ラ4","ミ4","ド4","ラ3"], "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    
    #此処を連れ出して
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #え～
    # {"value": "ミ4", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    ##サビ～##
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 抱き合って
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 最高潮よ
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 何時だって
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 騙し騙
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # しで良いの
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 代償なんて
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 気にしないよ
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ファ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    
    # # 愛憎愛憎
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # に足宛いて
    # {"value": "ソ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 外交愛想
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # # 振り撒いて
    # {"value": "ラ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #万物問答
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "レ4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # #無用で終いよ
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/16","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ド4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "Mute", "duration": "7/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #然らば又
    # {"value": "ファ#3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ソ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ラ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/4","velocity": MELODY_BASE_VELOCITY},
    # {"value": "シ3", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #逢いましょう
    # {"value": "ド4", "duration": "3/8","velocity": MELODY_BASE_VELOCITY},# 1/4 + 1/8 = 3/8
    # {"value": "レ4", "duration": "1/8","velocity": MELODY_BASE_VELOCITY},
    # {"value": "ミ4", "duration": "1/2","velocity": MELODY_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    #間奏
    #{"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
]
BASS = [
    # LUV ME LUV ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 愛憎愛憎
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # 渦巻いて
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #大東京狂騒
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #歌って
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #廻れ廻
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # れ時代の
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #生き恥に
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #ずぶ濡れで
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    # 愛憎愛憎
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # を喰らって
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #参ろう大層
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #な様で
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    # 離れ離
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},###
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド#3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ

    # れで終いよ
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド#3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # 然らば又
    {"value": "ファ#2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # 逢いましょう
    {"value": "ソ3", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ3", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "3/8", "velocity": BASS_BASE_VELOCITY},
    
    # 間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # ド
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # ラマチックに
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 溺れて 未完
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 成な私を
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 認めて 気休
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # めのフィク
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # ション 嘘と
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 真の不協和
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 音 出来損
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # な愛でも
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # 許して 構わ
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # ない 此の舞台
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # 生き抜いて 咬ま
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # せ狗のハイテン
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # ション ヤラレっ
    {"value": "ミ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # ぱなしじゃ 大人し
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},

    
    # くはなれない
    {"value": "ミ3", "duration": "1/1", "velocity": BASS_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #正しさばかりで
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #全部奪って
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #愛憎塗れで
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    #此処を連れ出して
    {"value": "Mute", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # え～
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 間奏
    {"value": "Mute", "duration": "1/1","velocity": MELODY_BASE_VELOCITY},
    
    # 愛憎愛憎
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # 抱き合って
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #最高潮よ
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #何時だって
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #騙し騙
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # しで良いの
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #代償なんて
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #気にしないよ
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    # 愛憎愛憎
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # に足宛いて
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    #外交愛想
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    #振り撒いて
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "シ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    
    # 万物問答
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ラ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド#3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ

    # 無用で終いよ
    {"value": "ソ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド#3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ソ2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    # 然らば又
    {"value": "ファ#2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},    
    {"value": "ファ#2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ド3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "レ3", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ#2", "duration": "1/8", "velocity": BASS_BASE_VELOCITY},
    
    
    {"value": "ファ2", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},##小節マタギ
    
    # 逢いましょう
    {"value": "ソ3", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ファ3", "duration": "1/4", "velocity": BASS_BASE_VELOCITY},
    {"value": "ミ3", "duration": "3/8", "velocity": BASS_BASE_VELOCITY},
]





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
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY}, 
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},#3弦
    {"value": "D5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "E5", "duration": "1/2", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ

    
    # HATE ME HATE ME
    {"value": "Mute", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    #間奏
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY}, 
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C6", "duration": "1/16", "velocity": GUITAR_BASE_VELOCITY},
   
    {"value": "D6", "duration": "7/16", "velocity": GUITAR_BASE_VELOCITY},#1/16 + 1/8+ 1/4 = 7/16 (小節マタギ)
    
    # LUV ME LUV ME
    {"value": "C6", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #間奏
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C6", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    {"value": "D5", "duration": "1/2", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
    
    # KILL ME KILL ME
    {"value": "Mute", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},


    
    #間奏
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},#３弦
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    #間奏
    {"value": "A5", "duration": "1/4","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    
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
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # れ時代の
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #生き恥に
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    
    #ずぶ濡れで
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
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
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # れで終いよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # 然らば又
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    
    # 逢いましょう
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # 間奏
    {"value": "A3", "duration": "6/4", "velocity": GUITAR_BASE_VELOCITY},##小節マタギ
    
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
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # 許して 構わ
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # ない 此の舞台
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # 生き抜いて 咬ま
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # せ狗のハイテン
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # ション ヤラレっ
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # ぱなしじゃ 大人し
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},

    
    # くはなれない
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},

    
    # LUV ME LUV ME
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #正しさばかりで
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # HATE ME HATE ME
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #全部奪って
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # LUV ME LUV ME
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #愛憎塗れで
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # KILL ME KILL ME
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    #此処を連れ出して
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    # え～
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "B4", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "D5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    {"value": "F5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G#5", "duration": "1/12", "velocity": GUITAR_BASE_VELOCITY},
    
    #間奏
    {"value": "A5", "duration": "1/4","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A4", "duration": "1/8","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/16","velocity": GUITAR_BASE_VELOCITY},
    
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
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # しで良いの
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    #代償なんて
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    
    #気にしないよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
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
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # 無用で終いよ
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "X", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "F5", "duration": "1/4", "velocity": GUITAR_BASE_VELOCITY},
    
    # 然らば又
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},    
    {"value": "C6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D6", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    
    
    
    # 逢いましょう
    {"value": "Mute", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "E5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "C5", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "G4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "D4", "duration": "1/8", "velocity": GUITAR_BASE_VELOCITY},
    {"value": "A3", "duration": "5/4", "velocity": GUITAR_BASE_VELOCITY},
]

# Drum events are placed with explicit beat positions.
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
    {"value": "Mute", "duration": "1/2", "velocity": DRUM_BASE_VELOCITY},
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
