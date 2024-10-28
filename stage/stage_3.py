import pygame
import os
import sys
from view.good_end import good_end
from view.bed_end import bed_end
from view.happy_end import happy_end

# 기본 질문 배열
dialogues = [
    {"dialogue": "첫번째 질문이야. 수뭉이의 생일은 ?", "portrait": "default.png"},
    {"dialogue": "두번째 질문이야, 수뭉이의 mbti는?", "portrait": "default.png"},
    {"dialogue": "다음 질문이야 이건 쉽지 않을 걸? 자 수뭉이 창조주의 성함은 뭐지?", "portrait": "default.png"},
    {"dialogue": "...마지막이야 수뭉이의 모티브가 된 동물은?", "portrait": "default.png"},
]

# 선택지에 따른 후속 대사 배열 (기본 질문 배열과 같은 인덱스)
dialogues_choice1 = [
    {"dialogue": "이건 쉬웠지", "portrait": "default.png"},
    {"dialogue": "오... 이건 꽤 어려웠을텐데", "portrait": "default.png"},
    {"dialogue": "허, 차준영... 너 진심이구나", "portrait": "default.png"},
    {"dialogue": "...약속한대로", "portrait": "default.png"},
]
dialogues_choice2 = [
    {"dialogue": "...! 바보얏... 그건 내 생일이라고...!", "portrait": "doki3.png"},
    {"dialogue": "그건 내 mbti잖아... 대체 모냐구...", "portrait": "doki.png"},
    {"dialogue": "너어... 차준영..! 나한테 왜이러는 거얏...", "portrait": "doki2.png"},
    {"dialogue": "바보! 멍청이! 변태!", "portrait": "doki3.png"},
]

# 선택지 배열
choices = [
    ["11월 28일", "9월 1일", "모르겠다"],
    ["ENFP", "INTP", "모르겠다"],
    ["신지우님", "민경록", "모르겠다"],
    ["사슴", "민경록", "모르겠다"]
]
choice_counts = {"choice_2": 0}  # 스페셜 엔딩 조건 확인


def stage3_text(screen):
    # 이미지 및 폰트 설정
    background = pygame.image.load(os.path.join('assets', 'images', 'backgrounds', 'stage3_background.png'))
    dialogue_box = pygame.image.load(os.path.join('assets', 'images', 'objects', 'stage3', 'stage3_textbox.png'))
    choice_box = pygame.image.load(os.path.join('assets', 'images', 'objects', 'stage3', 'stage3_choicebox.png'))
    portrait_box = pygame.image.load(os.path.join('assets', 'images', 'objects', 'stage3', 'stage3_portraitbox.png'))
    font_path = "assets/fonts/Galmuri14.ttf"
    font = pygame.font.Font(font_path, 30)
    max_width = 400

    def wrap_text(text):
        words = text.split(' ')
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            width, _ = font.size(' '.join(current_line))
            if width > max_width:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        return lines

    # 상태 변수 초기화
    dialogue_index = 0
    current_letter = 0
    show_all_text = False
    show_choices = False
    choice_selected = 0
    clock = pygame.time.Clock()
    current_dialogues = dialogues  # 기본 질문 배열로 시작

    while dialogue_index < len(dialogues):
        screen.fill((0, 0, 0))
        current_dialogue = current_dialogues[dialogue_index]

        # 배경 및 대화창 그리기
        screen.blit(background, (0, 0))
        if not show_choices:
            screen.blit(dialogue_box, (28, 14))
            dialogue_text = current_dialogue["dialogue"]
            portrait_image_path = os.path.join('assets', 'images', 'portrait', 'min', current_dialogue["portrait"])
            portrait_image = pygame.image.load(portrait_image_path).convert_alpha()
            screen.blit(portrait_box, (565, 332))
            screen.blit(portrait_image, (585, 359))

            max_lines = 3
            if not show_all_text:
                current_letter += 1
            wrapped_text = wrap_text(dialogue_text[:current_letter])
            for i, line in enumerate(wrapped_text[:max_lines]):
                line_surface = font.render(line, True, (0, 0, 0))
                screen.blit(line_surface, (87, 107 + i * 30))

            if current_letter >= len(dialogue_text):
                show_all_text = True

        # 선택지 표시
        if show_choices:
            for idx, choice_text in enumerate(choices[dialogue_index]):
                choice_pos = (56, 42 + idx * 180)
                choice_rect = pygame.Rect(choice_pos[0], choice_pos[1], 540, 175)
                if choice_selected == idx:
                    choice_image = pygame.transform.scale(choice_box, (500, 135))
                    choice_pos = (choice_pos[0] - 10, choice_pos[1] - 5)
                else:
                    choice_image = choice_box
                screen.blit(choice_image, choice_pos)
                choice_text_surface = font.render(choice_text, True, (255, 255, 255))
                screen.blit(choice_text_surface, (choice_pos[0] + 90, choice_pos[1] + 60))
                if choice_rect.collidepoint(pygame.mouse.get_pos()):
                    choice_selected = idx

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_choices:
                    # 선택지에 따라 후속 대사 출력 후 기본 질문으로 복귀
                    if choice_selected == 0:
                        current_dialogues = dialogues_choice1
                    elif choice_selected == 1:
                        choice_counts["choice_2"] += 1
                        if choice_counts["choice_2"] >= 2:
                            return "special_ending"
                        current_dialogues = dialogues_choice2
                    elif choice_selected == 2:
                        return "game_over"

                    # 후속 대사 후 다시 기본 질문으로 복귀
                    dialogue_index += 1  # 인덱스 증가
                    if dialogue_index >= len(dialogues):
                        return "good_ending"  # 모든 질문이 끝나면 굿 엔딩으로
                    current_dialogues = dialogues
                    current_letter = 0
                    show_choices = False

                elif show_all_text:
                    # 기본 질문이 끝나면 선택지 표시
                    show_choices = True
                    show_all_text = False
                    current_letter = 0

        pygame.display.update()
        clock.tick(40)


def stage_3(screen):
    ending = stage3_text(screen)
    if ending == "game_over":
        bed_end(screen)

    elif ending == "special_ending":
        happy_end(screen)

    elif ending == "good_ending":
        good_end(screen)
