import pygame
import os
import sys
from view.stage_3_intro import stage_3_intro


def stage_2(screen):
    background_path = "assets/images/backgrounds/stage2/stage2_background.png"
    platform_path = "assets/images/backgrounds/stage2/stage2map.png"
    collision_path = "assets/images/backgrounds/stage2/stage2map_hudle_color.png"
    key_image_path = "assets/images/objects/key.png"

    # 이미지 불러오기
    background_image = pygame.image.load(background_path).convert()
    platform_image = pygame.image.load(platform_path).convert_alpha()
    collision_image = pygame.image.load(collision_path).convert()
    key_image = pygame.image.load(key_image_path).convert_alpha()

    # 충돌 이미지 설정
    collision_image.set_colorkey((255, 255, 255))
    collision_data = pygame.surfarray.array3d(collision_image)

    # 키 관련 설정
    has_key = False
    key_rect = key_image.get_rect(topleft=(50, screen.get_height() // 2 - key_image.get_height() // 2))

    # 플레이어 설정
    player_width, player_height = 50, 75
    player_pos = [120, 80]
    player_speed = 25  # 3배 빠르게
    jump_speed = -8  # 점프 속도 증가
    gravity = 1.4  # 중력 증가
    velocity_y = 0
    is_jumping = False

    # 애니메이션 설정
    run_images = [
        pygame.image.load(os.path.join("assets/images/character/stage2/run", f"run2_{i + 1}.png")).convert_alpha() for i
        in range(5)]
    jump_images = [
        pygame.image.load(os.path.join("assets/images/character/stage2/jump", f"jump2_{i + 1}.png")).convert_alpha() for
        i in range(7)]
    standing_image = pygame.image.load(os.path.join("assets/images/character/stage2/standing2.png")).convert_alpha()
    animation_index = 0
    current_motion = "standing"
    current_image = standing_image

    # 목표 위치 설정 (파란색이 목표 영역)
    goal_rect = None
    for y in range(collision_image.get_height()):
        for x in range(collision_image.get_width()):
            color = tuple(collision_data[x, y])
            if color == (0, 5, 255):  # 파란색으로 목표 지점 표시
                goal_rect = pygame.Rect(x, y, 20, 20)

    # 플랫폼 위치 설정
    platforms = [
        pygame.Rect(x, y, 1, 1)
        for y in range(collision_image.get_height())
        for x in range(collision_image.get_width())
        if tuple(collision_data[x, y]) == (0, 0, 0)  # 검은색으로 플랫폼 표시
    ]

    # 벽 설정 (벽에 부딪히면 이동 멈추게)
    walls = [
        pygame.Rect(x, y, 1, 1)
        for y in range(collision_image.get_height())
        for x in range(collision_image.get_width())
        if tuple(collision_data[x, y]) == (255, 255, 0)  # 노란색으로 벽 표시
    ]

    # 게임 상태 변수
    game_won = False
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # 배경 이미지
        screen.blit(platform_image, (0, 0))  # 맵 이미지
        if not has_key:
            screen.blit(key_image, key_rect.topleft)  # 키 이미지

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    velocity_y = jump_speed
                    is_jumping = True
                    current_motion = "jump"

        # 중력 적용
        velocity_y += gravity
        player_pos[1] += velocity_y

        # 키보드 입력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_pos[0] -= player_speed
            current_motion = "run"
            animation_index = (animation_index + 1) % len(run_images)
            current_image = run_images[animation_index]

        elif keys[pygame.K_d]:
            player_pos[0] += player_speed
            current_motion = "run"
            animation_index = (animation_index + 1) % len(run_images)
            current_image = run_images[animation_index]
        else:
            if not is_jumping:
                current_motion = "standing"
                current_image = standing_image

        # 플레이어 충돌 처리
        player_rect = pygame.Rect(player_pos[0], player_pos[1], player_width, player_height)

        # 플랫폼 충돌
        for platform in platforms:
            if player_rect.colliderect(platform) and velocity_y > 0:
                player_pos[1] = platform.y - player_height
                velocity_y = 0
                is_jumping = False
            elif player_rect.colliderect(platform) and velocity_y < 0:
                player_pos[1] = platform.y + platform.height
                velocity_y = 0.1  # 천장에서 튕기기

        # 벽 충돌
        for wall in walls:
            if player_rect.colliderect(wall):
                if keys[pygame.K_a]:  # 왼쪽 이동 중일 때
                    player_pos[0] = wall.right
                elif keys[pygame.K_d]:  # 오른쪽 이동 중일 때
                    player_pos[0] = wall.left - player_width

        # 천장 탈출 방지
        if player_pos[1] < 0:
            player_pos[1] = 0
            velocity_y = 0.1

        # 위험 요소 충돌 처리
        for y in range(collision_image.get_height()):
            for x in range(collision_image.get_width()):
                if tuple(collision_data[x, y]) == (255, 28, 0):  # 빨간색으로 위험 요소 표시
                    hazard_rect = pygame.Rect(x, y, 1, 1)
                    if player_rect.colliderect(hazard_rect):
                        player_pos = [120, 80]
                        velocity_y = 0
                        has_key = False

        # 키 획득 처리
        if not has_key and player_rect.colliderect(key_rect):
            has_key = True

        # 목표 지점 도달 처리
        if goal_rect and player_rect.colliderect(goal_rect):
            if has_key:
                game_won = True
                running = False
            else:
                player_pos = [120, 80]  # 시작 위치로 돌아감

        # 목표 지점 그리기
        if goal_rect:
            pygame.draw.rect(screen, (0, 5, 255), goal_rect)

        # 캐릭터 애니메이션
        if current_motion == "jump":
            current_image = jump_images[min(int(abs(velocity_y) // 2), len(jump_images) - 1)]

        # 플레이어 그리기
        screen.blit(current_image, player_pos)

        pygame.display.flip()
        clock.tick(60)

    if game_won:
        stage_3_intro(screen)
    else:
        print("게임이 종료되었습니다.")
