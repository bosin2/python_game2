import pygame
import os
import sys
from logic.dialogue_display import dialogue_display
from logic.transition_effect import transition_effect
from stage.stage_2 import stage_2


dialogues = [
    {"backgrounds": "black_background.png", "cha": "default.png", "name": "차준영",
     "dialogue": "여기는...?"},
    {"backgrounds": "stage2_background.png", "cha": "dis.png", "name": "차준영",
     "dialogue": "..."},
    {"backgrounds": "stage2_background.png", "cha": "dis.png", "name": "차준영",
     "dialogue": "...아니 이렇게까지 해야하는거냐고... 일단 가보자..."},
]


def stage_2_intro(screen):

    background_path = "assets/images/backgrounds/stage2"
    font_path = "assets/fonts/Galmuri14.ttf"
    screen_image_path = "assets/images/backgrounds/stage1_5.png"

    transition_effect(screen, screen_image_path)
    dialogue_display(screen, dialogues, background_path, font_path)

    stage_2(screen)