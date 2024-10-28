import pygame
import os
import sys
from stage.stage_1 import stage_1
from logic.dialogue_display import dialogue_display

# 대사 데이터 정의
dialogues = [
    {"backgrounds": "black_background.png", "cha": "what.png", "name": "차준영",
     "dialogue": "하아... 너무 힘들다... 아 파이썬 왜 이리 어려운거지"},
    {"backgrounds": "black_background.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(터벅... 터벅...)"},
    {"backgrounds": "black_background.png", "cha": "what.png", "name": "차준영",
     "dialogue": "에휴..."},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "..."},
    {"backgrounds": "way1.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(힐끗)"},
    {"backgrounds": "way2.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(힐끗)"},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "...아무도 없겠지?"},
    {"backgrounds": "way.png", "cha": "default.png", "name": "차준영",
     "dialogue": "후우... 자 그럼..."},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(털석)"},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "(부시럭.. 부시럭...)"},
    {"backgrounds": "cha.png", "cha": "default.png", "name": "차준영",
     "dialogue": "어디에 뒀더라? 음... 여긴가... 설마, 박스가 깔린건... "},
    {"backgrounds": "black_background.png", "cha": "happy.png", "name": "차준영",
     "dialogue": "아, 찾았다 !"},
    {"backgrounds": "black_background.png", "cha": "shy.png", "name": "차준영",
     "dialogue": "오... 오오오 ! 나, 나의....."},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "상명대 설립 86주년 특별 기획 리미티드 에디션- 수뭉이 탄생 3주년 기념 초회 한정판...!!!"
                 "처음 공개되는 핑크 수뭉이 버전으로 오직 10개만 생산되며"},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "수뭉이 생일 6개월 전부터 치밀한 예약 전쟁이...! 크흑...! 아x묭 콘서트 잡기보다 어려웠다고! "
                 "선착순 10명에게만 제공되는 이 선배송의 혜택...!"},
    {"backgrounds": "wow.png", "cha": "lovelove.png", "name": "차준영",
     "dialogue": "쓰읍... 하아. 킁킁... 이 영롱한 자태... 너무 아름다워...! "
                 "학교로 밖에 배송되지 않아서 고민했는데, 사길... 잘했다!"},
    {"backgrounds": "wow.png", "cha": "verycry.png", "name": "차준영",
     "dialogue": "아아... 너무 아름다워서 눈물이 날 것만 같아..."},
    {"backgrounds": "black_background.png", "name":" ",
     "dialogue": "웅성... 웅성..."},
    {"backgrounds": "ele.png","name":" ",
     "dialogue": "띵 !"},
    {"backgrounds": "ele2.png","name":" ",
     "dialogue": "저벅... 저벅..."},
    {"backgrounds": "ele2.png", "min": "angry.png", "name": "민경록",
     "dialogue": "...아니 들어보라고. 아 진짜, 아... 진짜 어떻게 나즈나보다 사기가 어렵냐? 하"},
    {"backgrounds": "ele2.png", "my": "my.png", "name": "박조화",
     "dialogue": "민경록아. 무슨 수뭉이 피규어냐. 그럴 바에는 나의 사랑스러운 렘땅의 피규어를 삼"},
    {"backgrounds": "ele2.png", "min": "default.png", "name": "민경록",
     "dialogue": "조화야. 넌 좀 조용히하라고"},
    {"backgrounds": "ele2.png", "jeong": "jeong1.png", "name": "정은찬",
     "dialogue": "경록아 나는 이해해 그럴 수 있지...ㅋ"},
    {"backgrounds": "ele2.png", "min": "angry.png", "name": "민경록",
     "dialogue": "아니;;;"},
    {"backgrounds": "black_background.png", "my": "my.png", "name": "박조화",
     "dialogue": "어?"},
    {"backgrounds": "way3.png", "my": "my.png", "name": "박조화",
     "dialogue": "어 !!!  저거 차차차차준영이 아니냐? 야 차차차차준영 거기서 뭐해"},
    {"backgrounds": "way3.png", "cha": "sup.png", "name": "차준영",
     "dialogue": "!!!"},
    {"backgrounds": "way3.png", "cha": "what.png", "name": "차준영",
     "dialogue": "어...? 너, 너희 수업 아,아니냐?"},
    {"backgrounds": "way3.png", "jeong": "jeong1.png", "name": "정은찬",
     "dialogue": "엇! 손에 들고 있는 그거... 수...뭉이...? 엥, 경록아 저거 니가 찾던거 아니야?"},
    {"backgrounds": "wow.png", "min": "sup.png", "name": "민경록",
     "dialogue": "!!!"},
    {"backgrounds": "wow.png", "cha": "what.png", "name": "차준영",
     "dialogue": "아, 아니 무슨 소리야 하하... 그게 뭔데 난 몰라..."},
    {"backgrounds": "wow.png", "my": "my.png", "name": "박조화",
     "dialogue": "ㅋㅋㅋㅋ 차차차차차준영이 너 그런 취향이었냐?"},
    {"backgrounds": "wow.png", "min": "stop.png", "name": "민경록",
     "dialogue": "준영아..."},
    {"backgrounds": "wow.png", "cha": "what.png", "name": "차준영",
     "dialogue": "..."},
    {"backgrounds": "way3.png", "jeong": "jeong1.png", "name": "정은찬",
     "dialogue": "이 분위기 뭐야... 난 과방으로 갈래..."},
    {"backgrounds": "way3.png", "my": "my.png", "name": "박조화",
     "dialogue": "둘이 이쁜 사랑해라 ㅋㅋ 은찬아 가자"},
    {"backgrounds": "way3.png", "min": "tremble.png", "name": "민경록",
     "dialogue": "...준영아 미안하다...!"},
    {"backgrounds": "way4.png", "cha": "what.png", "name": "차준영",
     "dialogue": "어...?? 어...!!!!"},
    {"backgrounds": "thief.png", "cha": "sup.png", "name": "차준영",
     "dialogue": "야..! 아니, 뭔, 무슨, 민,민경록!!!!!!!!!! 이, 정,신나간!!!!!!!!!!"},
    {"backgrounds": "thief.png", "min": "tremble2.png", "name": "민경록",
     "dialogue": "...미안하다. 돈은 입금하마. 형 간다"},
    {"backgrounds": "run.png", "cha": "sup.png", "name": "차준영",
     "dialogue": "야!!!!!!!!!! 거기서!!!!!!"},
    {"backgrounds": "run.png", "cha": "angry.png", "name": "차준영",
     "dialogue": "민경록 !!! 내 수뭉이 피규어 돌려줘 !!!!!!!!"},
    {"backgrounds": "black_background.png", "cha": "angry.png", "name": "차준영",
     "dialogue": "빨리 쫓아가자 !"},
]


def go_to_next_screen(screen):
    stage_1(screen)


def start_intro(screen):
    background_path = "assets/images/backgrounds/stage1_intro"
    font_path = "assets/fonts/Galmuri14.ttf"
    dialogue_display(screen, dialogues, background_path, font_path)
    go_to_next_screen(screen)
