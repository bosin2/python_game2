import pygame
import sys
import os


def transition_effect(screen, screen_image_path):
    screen_image = pygame.image.load(screen_image_path)
    black = (0, 0, 0)
    fps = 60
    clock = pygame.time.Clock()

    # 애니메이션 설정
    transition_duration = 3000  # 애니메이션 지속 시간 (밀리초)
    start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        progress = elapsed_time / transition_duration  # 진행률 (0에서 1 사이)

        if progress > 1:
            break  # 애니메이션 종료

        # 알파 값 계산 (255에서 0으로 감소)
        alpha = int(255 * (1 - progress))
        fade_surface = screen_image.copy()
        fade_surface.set_alpha(alpha)

        screen.fill(black)
        screen.blit(fade_surface, (0, 0))

        pygame.display.update()
        clock.tick(fps)

    print("Exiting transition_effect function.")  # 종료 디버깅 메시지
