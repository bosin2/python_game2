import pygame
import os
import sys
from logic.dialogue_display import dialogue_display
from logic.transition_effect import transition_effect
from stage.stage_1_5 import stage_1_5

dialogues = [
    {"backgrounds": "black_background.png", "cha": "him.png", "name": "차준영",
     "dialogue": "헉...헉 멈, 춰 민경,록...! 수뭉이, 돌려줘...!"},
    {"backgrounds": "black_background.png", "min": "mu.png", "name": "민경록",
     "dialogue": "..."},
    {"backgrounds": "stage1_5_intro2.png", "min": "mu.png", "name": "민경록",
     "dialogue": "..."}
]

dialogues2 = [
    {"backgrounds": "black_background.png", "cha": "angry.png", "name": "차준영",
     "dialogue": "뭐야? 대답도 안하고 그냥 가잖아!"},
    {"backgrounds": "black_background.png", "cha": "default.png", "name": "차준영",
     "dialogue": "하... 화낼 시간도 아깝네... 빨리 쫓아가자"},
    {"backgrounds": "stage1_5.png", "cha": "default.png", "name": "차준영",
     "dialogue": "흠... 비밀번호가 뭘까. 분명 단순한거겠지... 주변을 둘러보자"},
]


def stage_1_5_intro(screen):
    background_path = "assets/images/backgrounds/stage1_5_intro"
    font_path = "assets/fonts/Galmuri14.ttf"
    screen_image_path = "assets/images/backgrounds/stage1_5_intro/stage1_5_intro.png"

    dialogue_display(screen, dialogues, background_path, font_path)
    transition_effect(screen, screen_image_path)
    dialogue_display(screen, dialogues2, background_path, font_path)

    stage_1_5(screen)
