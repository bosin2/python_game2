import pygame
import os
import sys
from logic.dialogue_display import dialogue_display

dialogues = [
    {"backgrounds": "black_background.png", "min": "default.png", "name": "민경록",
     "dialogue": "너는 자격이잇어준영아 수뭉이를돌려줄게"},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "cry.png",
     "dialogue": "어어 고마워 경록아"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "잘가 수뭉아 ㅠㅠ"},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "cry.png",
     "dialogue": "너도 수뭉이를 만날수잇을거야"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "곰아워요 곰아워요"},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "진엔딩 ~사이 좋은 결말~"},

]


def good_end(screen):

    background_path = "assets/images/backgrounds/stage3"
    font_path = "assets/fonts/Galmuri14.ttf"

    dialogue_display(screen, dialogues, background_path, font_path)

    pygame.quit()
