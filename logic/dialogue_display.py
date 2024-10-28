import pygame
import sys
import os


def dialogue_display(screen, dialogues, background_path, font_path):
    # 폰트와 대화창 가로 길이를 설정
    font = pygame.font.Font(font_path, 20)
    max_width = 500  # 대화창 가로 길이에 맞게 설정

    def wrap_text(text):
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            # 현재 라인의 길이를 계산
            width, _ = font.size(' '.join(current_line))
            if width > max_width:
                # 줄이 너무 길면 마지막 단어를 다음 줄로 넘김
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]

        lines.append(' '.join(current_line))
        return lines

    # 대화창 이미지 불러오기
    dialogue_box_image = pygame.image.load(os.path.join('assets', 'images', 'dialogue_box.png'))
    font = pygame.font.Font(font_path, 20)

    # 현재 대사와 상황
    dialogue_index = 0
    current_letter = 0
    show_all_text = False  # 한 번에 다 보여주기 위한 플래그
    clock = pygame.time.Clock()

    while dialogue_index < len(dialogues):
        screen.fill((0, 0, 0))  # 화면 초기화

        portrait_image = None

        # 대화 상황 불러오기
        current_dialogue = dialogues[dialogue_index]
        background_image = pygame.image.load(os.path.join(background_path, current_dialogue['backgrounds']))
        if 'cha' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'cha', current_dialogue['cha']))
        elif 'min' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'min', current_dialogue['min']))
        elif 'jeong' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'jeong', current_dialogue['jeong']))
        elif 'my' in current_dialogue:
            portrait_image = pygame.image.load(
                os.path.join('assets', 'images', 'portrait', 'my', current_dialogue['my']))

        name = current_dialogue['name']
        dialogue = current_dialogue['dialogue']

        # 배경 그리기
        screen.blit(background_image, (0, 0))

        # 대화창과 초상화 그리기
        screen.blit(dialogue_box_image, (0, 365))  # 대화창 위치 설정
        if portrait_image is not None:
            screen.blit(portrait_image, (7, 381))  # 초상화 위치 설정

        # 캐릭터 이름 출력
        name_surface = font.render(name, True, (255, 255, 255))
        screen.blit(name_surface, (240, 415))  # 이름 위치 설정

        # 대사 출력 (줄바꿈 처리)
        max_width = 500  # 대사창 가로 길이에 맞게 설정
        max_lines = 3  # 대화창에 표시될 최대 줄 수

        if not show_all_text:
            current_letter += 1

        wrapped_text = wrap_text(dialogue[:current_letter])

        for i, line in enumerate(wrapped_text[:max_lines]):
            line_surface = font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (230, 470 + i * 30))  # 대사 위치 (줄마다 Y 위치 변경)

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if show_all_text:  # 대사 전체가 이미 출력되었으면 다음 대사로 넘어감
                    dialogue_index += 1
                    current_letter = 0
                    show_all_text = False
                else:
                    show_all_text = True  # 한 번에 대사 전부 출력

        # 대사가 모두 출력되면 대사 넘기기 플래그 설정
        if current_letter >= len(dialogue):
            show_all_text = True

        pygame.display.update()
        clock.tick(40)  # 프레임 속도 조절

