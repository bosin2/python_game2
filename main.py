import pygame
import sys
from menu.main_menu import main_menu  # main_menu 함수 불러오기
from stage.stage_1_5 import stage_1_5  # 새로 만든 스테이지 파일을 불러옴
from stage.stage_1 import stage_1
from stage.stage_2 import stage_2
from stage.stage_3 import stage_3


def main():
    # Pygame 초기화
    pygame.init()

    # 화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("민경록, 내 수뭉이 피규어 돌려줘!")

    # 메인 메뉴 함수 호출
    main_menu(screen)


if __name__ == "__main__":
    main()
