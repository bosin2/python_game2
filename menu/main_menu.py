import pygame
import sys
from view.start_intro import start_intro  # 인트로 화면 불러오기
import os


def main_menu(screen):
    # 배경 이미지 불러오기
    background_image = pygame.image.load(os.path.join('assets', 'images', 'backgrounds', 'mainscreen.png'))

    running = True
    while running:
        # 배경 이미지 그리기
        screen.blit(background_image, (0, 0))

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 클릭 시 다음 화면으로
                start_intro(screen)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # 스페이스바 입력 시 다음 화면으로
                    start_intro(screen)
                    running = False

        pygame.display.update()
