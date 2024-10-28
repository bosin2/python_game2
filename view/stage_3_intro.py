import pygame
import os
import sys
from logic.dialogue_display import dialogue_display
from stage.stage_3 import stage_3
dialogues = [
    {"backgrounds": "black_background.png", "cha": "cry.png", "name": "차준영",
     "dialogue": "아아...드디어...!!"},
    {"backgrounds": "white_background.png", "name": "",
     "dialogue": "문이 열린다"},
    {"backgrounds": "white_background.png", "name": "민경록",
     "dialogue": "...진짜 여기까지 왔네"},
    {"backgrounds": "white_background.png", "name": "차준영", "cha": "angry.png",
     "dialogue": "민경록!!!!! 내 수뭉이 피규어 돌려줘!!!!"},
    {"backgrounds": "stage3_background.png", "name": "차준영", "cha": "angry.png",
     "dialogue": "내놔 !!!!"},
    {"backgrounds": "stage3_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "쉽게 줄 수 는 없지. 수뭉이의 파트너가 될 자격이 있는지 확인해야겠어. "},
    {"backgrounds": "white_background.png", "name": "차준영", "cha": "angry.png",
     "dialogue": "아니 원래 내꺼라고! 정신나간거 아니야?"},
    {"backgrounds": "stage3_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "자 첫번째 질문이야"},

]


def stage_3_intro(screen):

    background_path = "assets/images/backgrounds/stage3"
    font_path = "assets/fonts/Galmuri14.ttf"

    dialogue_display(screen, dialogues, background_path, font_path)

    stage_3(screen)