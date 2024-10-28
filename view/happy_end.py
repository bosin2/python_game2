import pygame
import os
import sys
from logic.dialogue_display import dialogue_display

dialogues = [
    {"backgrounds": "black_background.png", "min": "default.png", "name": "민경록",
     "dialogue": "...준영아 넌... 사실 수뭉이가 아니라 나를...?"},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "default.png",
     "dialogue": "...그러면 너는? 사실 난 알고 있었어"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "..."},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "default.png",
     "dialogue": "경록아..."},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "준영아..."},
    {"backgrounds": "black_background.png", "name": "차준영", "cha": "default.png",
     "dialogue": "(나는 경록이의 사랑스러운 눈을 마주보며 무언의 질문에 답을 했다) 응..!"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "!"},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "경록이가 싱긋 웃는다"},
    {"backgrounds": "black_background.png", "name": "민경록", "min": "default.png",
     "dialogue": "... 가자 준영아"},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "우리 둘은 서로 숨을 죽이며, 손을 마주잡고, ..."},
    {"backgrounds": "black_background.png", "name": "",
     "dialogue": "리얼 엔딩 ~수뭉이: 행복하게 잘 살아~"},

]


def happy_end(screen):

    background_path = "assets/images/backgrounds/stage3"
    font_path = "assets/fonts/Galmuri14.ttf"

    dialogue_display(screen, dialogues, background_path, font_path)

    pygame.quit()
