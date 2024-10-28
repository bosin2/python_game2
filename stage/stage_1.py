import pygame, sys, random, os
from pygame.locals import *
from view.stage_1_5_intro import stage_1_5_intro
from logic.transition_effect import transition_effect

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
assets_dir = 'assets'
images_dir = os.path.join(assets_dir, 'images')
sounds_dir = os.path.join(assets_dir, 'sounds')
screen_image_path = os.path.join(images_dir, 'backgrounds', 'stage1_outro.png')

# 색상
WHITE = (255, 255, 255)

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

heart_images = {
    'full': pygame.image.load(os.path.join(images_dir, 'objects', 'heart_full.png')),
    'empty': pygame.image.load(os.path.join(images_dir, 'objects', 'heart_empty.png'))
}
heart_images['full'] = pygame.transform.scale(heart_images['full'], (50, 50))
heart_images['empty'] = pygame.transform.scale(heart_images['empty'], (50, 50))

min_obstacle_gap = 300


# 게임 종료 화면
def show_game_over():
    game_over_image = pygame.image.load(os.path.join(images_dir, 'backgrounds', 'gameover.png'))
    screen.blit(game_over_image, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


# 이미지 로드 함수
def load_images(folder, prefix, count, size=None):
    images = []
    for i in range(1, count + 1):
        image_path = os.path.join('assets', 'images', folder, f'{prefix}{i}.png')
        image = pygame.image.load(image_path)
        if size:
            image = pygame.transform.scale(image, size)
        images.append(image)
    return images


# 플레이어 객체 설정
def create_player():
    player_rect = pygame.Rect((SCREEN_WIDTH - 100) / 5, 457 - 150, 100, 150)
    player_images = {
        'run': load_images('character/run', 'run', 6, (100, 150)),
        'jump': load_images('character/jump', 'jump', 6, (100, 150)),
        'slide': load_images('character/sliding', 'sliding', 4, (150, 100))
    }
    # 마스크 생성
    player_masks = {
        'run': [pygame.mask.from_surface(img) for img in player_images['run']],
        'jump': [pygame.mask.from_surface(img) for img in player_images['jump']],
        'slide': [pygame.mask.from_surface(img) for img in player_images['slide']]
    }
    return player_rect, player_images, player_masks


def create_obstacle(obstacles, bottom_obstacles, top_obstacles):
    if not obstacles or obstacles[-1][0].x <= SCREEN_WIDTH - min_obstacle_gap:
        obstacle_type = random.choice(['bottom', 'top'])
        if obstacle_type == 'bottom':
            obstacle_image = random.choice(bottom_obstacles)
            obstacle = pygame.Rect(SCREEN_WIDTH, 457 - 80, 80, 80)  # 하단 장애물 높이에 맞게 조정
        else:
            obstacle_image = random.choice(top_obstacles)
            obstacle = pygame.Rect(SCREEN_WIDTH, -5, 140, 330)  # 상단 장애물 높이에 맞게 조정
        obstacle_mask = pygame.mask.from_surface(obstacle_image)  # 장애물 마스크 생성
        obstacles.append((obstacle, obstacle_image, obstacle_mask))


# 목숨 표시 함수
def draw_hearts(heart_count):
    for i in range(3):
        heart_image = heart_images['full'] if i < heart_count else heart_images['empty']
        screen.blit(heart_image, (i * 50, 0))


def next_stage():
    black_image = pygame.image.load(os.path.join(images_dir, 'backgrounds', 'black_background.png'))
    screen.blit(black_image, (0, 0))
    pygame.time.delay(2000)
    stage_1_5_intro(screen)


# 메인 게임 함수
def stage_1(screen):
    background_images = load_images('backgrounds/stage1_background', 'stage1_backgroun_', 31, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_index = 0
    last_background_change = pygame.time.get_ticks()
    background_change_time = 100

    player, player_images, player_masks = create_player()
    player_state = 'run'
    image_index = 0
    last_image_change = pygame.time.get_ticks()

    sliding_duration = 1200
    sliding_start_time = None

    obstacles = []
    last_obstacle_time = pygame.time.get_ticks()
    bottom_obstacles = load_images('objects/hurdle_down', 'hurdle_down', 2, (80, 80))
    top_obstacles = load_images('objects/hurdle_up', 'hurdle', 2, (140, 330))

    heart_count = 3
    y_vel = 0
    is_sliding, is_jumping = False, False

    jump_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'jump.mp3'))
    sliding_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'sliding.mp3'))
    jump_sound.set_volume(0.3)
    sliding_sound.set_volume(0.3)

    start_time = pygame.time.get_ticks()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if heart_count <= 0:
            show_game_over()

        current_time = pygame.time.get_ticks()

        # 시간경과체크
        elapsed_time = (current_time - start_time) / 1000  # 초 단위로 변환
        if elapsed_time >= 10:
            transition_effect(screen, screen_image_path)  # 화면 전환 효과 실행
            next_stage()  # 다음 화면으로 전환
            break  # 게임 루프 종료

        if current_time - last_background_change >= background_change_time:
            background_index = (background_index + 1) % len(background_images)
            last_background_change = current_time
        screen.blit(background_images[background_index], (0, 0))

        if current_time - last_image_change >= 100:
            image_index = (image_index + 1) % len(player_images[player_state])
            last_image_change = current_time

        if len(player_images[player_state]) > 0:
            image_index %= len(player_images[player_state])
        else:
            image_index = 0

        player_mask = player_masks[player_state][image_index]  # 현재 프레임의 플레이어 마스크

        keys = pygame.key.get_pressed()
        if keys[K_j] and not is_jumping and not is_sliding:
            is_jumping, player_state = True, 'jump'
            image_index = 0  # 인덱스 초기화
            jump_sound.play()
            y_vel = -18

        if keys[K_k] and not is_jumping and not is_sliding:
            is_sliding, player_state = True, 'slide'
            image_index = 0  # 인덱스 초기화
            sliding_sound.play()
            player.height = 100
            player.bottom = 457
            sliding_start_time = pygame.time.get_ticks()

        if is_sliding:
            player.height = 100
            player.bottom = 457
            if current_time - sliding_start_time >= sliding_duration:
                is_sliding = False
                player_state = 'run'
                image_index = 0
                player.height = 150
                player.top = 457 - 150

        if is_jumping:
            player.top += y_vel
            y_vel += 1
            if player.bottom >= 457:
                player.bottom = 457
                is_jumping = False
                player_state = 'run'
                image_index = 0
                player.height = 150
                player.top = 457 - 150
                y_vel = 0

        # 장애물 생성 및 이동
        if current_time - last_obstacle_time >= random.randint(700, 1500):
            create_obstacle(obstacles, bottom_obstacles, top_obstacles)
            last_obstacle_time = current_time

        new_obstacles = []
        for obstacle, image, obstacle_mask in obstacles:
            obstacle.x -= 5
            screen.blit(image, obstacle)

            # 마스크 충돌 검사
            offset = (obstacle.x - player.x, obstacle.y - player.y)
            if player_mask.overlap(obstacle_mask, offset):
                heart_count -= 1
            elif obstacle.right >= 0:
                new_obstacles.append((obstacle, image, obstacle_mask))

        obstacles = new_obstacles
        screen.blit(player_images[player_state][image_index], player)

        draw_hearts(heart_count)
        pygame.display.update()
        clock.tick(FPS)
