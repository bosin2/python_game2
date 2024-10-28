import pygame
import os
import sys
from logic.dialogue_display import dialogue_display

dialogues = [
    {"backgrounds": "black_background.png", "min": "default.png", "name": "민경록",
     "dialogue": "넌안되겠다 (수뭉이피규어를부순다)"},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "cry.png",
     "dialogue": "어 안돼 내 수뭉이"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "잘가라. 자격없는 사람한테 넘길수는 없지"},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "그렇게 수뭉이는 생을 마감했다..."},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "cry.png",
     "dialogue": "어흑흑 어흑흑 나의 수뭉이 쟈응"},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "베드엔딩 ~자격없는 자~"},

]


def bed_end(screen):

    background_path = "assets/images/backgrounds/stage3"
    font_path = "assets/fonts/Galmuri14.ttf"

    dialogue_display(screen, dialogues, background_path, font_path)

    pygame.quit()
