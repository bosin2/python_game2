import pygame
import sys
import os
from view.stage_2_intro import stage_2_intro


def stage_1_5(screen):

    # 이미지 불러오기
    background = pygame.image.load(os.path.join('assets', 'images', 'backgrounds', 'stage1_5.png'))
    dialogue_box_image = pygame.image.load(os.path.join('assets', 'images', 'dialogue_box.png'))

    input_active_color = (0, 100, 200)
    input_inactive_color = (255, 255, 255)

    # 폰트 설정 (커스텀 폰트 경로)
    font_path = os.path.join('assets', 'fonts', 'Galmuri14.ttf')
    font_path2 = os.path.join('assets', 'fonts', 'Galmuri11-Bold.ttf')
    font = pygame.font.Font(font_path, 20)
    font2 = pygame.font.Font(font_path2, 30)

    # 대화 상태 변수
    is_dialogue_active = False
    current_dialogue_index = 0  # 현재 대화의 인덱스
    current_object = None  # 현재 클릭된 오브젝트

    password_input_active = False
    user_input = ""  # 사용자가 입력한 비밀번호
    correct_password = "2952"
    # 오브젝트 정보 (이미지, 위치, 이벤트)
    objects = [
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'lock.png')), "pos": (297, 330),
         "event": "lock"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'album.png')), "pos": (112, 544),
         "event": "album"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'album2.png')), "pos": (688, 512),
         "event": "album2"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'calendar.png')), "pos": (250, 510),
         "event": "calendar"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'calendar2.png')), "pos": (450, 530),
         "event": "calendar2"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'nazna.png')), "pos": (400, 467),
         "event": "nazna"},
        {"image": pygame.image.load(os.path.join('assets', 'images', 'objects', 'memo.png')), "pos": (610, 328),
         "event": "memo"}
    ]

    def dialogue_album():
        return [
            {"name": "", "dialogue": "민경록의 앨범이다"},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "으... 보기 싫어"},
            {"name": "차준영", "portrait": "default.png", "dialogue": "음? 이게 뭐지..."},
            {"name": "", "dialogue": "민경록이 나즈나, 수뭉이와 찍은 사진이다"},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "우웨엑..."}
        ]

    def dialogue_album2():
        return [
            {"name": "", "dialogue": "수뭉이의 앨범이다"},
            {"name": "차준영", "portrait": "lovelove.png", "dialogue": "역시 수뭉이는 귀여웟...!"}
        ]

    def dialogue_calendar():
        return [
            {"name": "", "dialogue": "민경록이 쓰는 달력이다."},
            {"name": "", "dialogue": "9월 1일에 동그라미가 쳐져있다"},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "생일 따위 알고싶지 않아..."}
        ]

    def dialogue_calendar2():
        return [
            {"name": "차준영", "portrait": "default.png", "dialogue": "이건..."},
            {"name": "", "dialogue": "민경록이 만든 수뭉이 전용 달력이다..."},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "진짜 극혐"},
            {"name": "", "dialogue": "수뭉이의 생일인 11월 28일에 동그라미가 쳐져있다"},
            {"name": "", "dialogue": "...다른 페이지에는 알 수 없는 곳에 하트가 쳐져있다"}

        ]

    def dialogue_nazna():
        return [
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "으아... 이게 뭐야?"},
            {"name": "", "dialogue": "경록이의 최애, 나즈나 인형이다"},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "으 극혐..."},
            {"name": "차준영", "portrait": "default.png", "dialogue": "엇 뒤에 뭐가 달려있네"},
            {"name": "", "dialogue": "인형 뒤에는 9월 23일 이라 적혀있다"}

        ]

    def dialogue_memo():
        return [
            {"name": "차준영", "portrait": "default.png", "dialogue": "흠... 메모가 있네"},
            {"name": "차준영", "portrait": "default.png", "dialogue": "경..록이가 좋아하는 것들..?"},
            {"name": "차준영", "portrait": "dislike.png", "dialogue": "뭔, 누가 해둔거야?"}
        ]

    def lock_event():
        nonlocal password_input_active, user_input
        password_input_active = True  # 비밀번호 입력 활성화
        user_input = ""  # 입력 초기화

    def draw_password_input(screen, font, user_input, active_color, inactive_color, is_active):
        # 입력창 위치와 크기 설정
        input_box = pygame.Rect(300, 200, 200, 50)
        # 입력창 색상 설정
        color = active_color if is_active else inactive_color
        # 배경 색상 그리기
        pygame.draw.rect(screen, (0, 0, 0), input_box)  # 검은색 배경
        # 테두리 그리기
        pygame.draw.rect(screen, color, input_box, 2)  # 테두리 두께 2px

        # 사용자 입력 텍스트
        text_surface = font.render(user_input, True, (255, 255, 255))  # 흰색 텍스트
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    def handle_object_click(event):
        nonlocal is_dialogue_active, current_dialogue_index, current_object
        if event == "lock":
            lock_event()
        elif event == "album":
            current_object = {"dialogues": dialogue_album()}
            is_dialogue_active = True
            current_dialogue_index = 0
        elif event == "album2":
            current_object = {"dialogues": dialogue_album2()}
            is_dialogue_active = True
            current_dialogue_index = 0
        elif event == "calendar":
            current_object = {"dialogues": dialogue_calendar()}
            is_dialogue_active = True
            current_dialogue_index = 0
        elif event == "calendar2":
            current_object = {"dialogues": dialogue_calendar2()}
            is_dialogue_active = True
            current_dialogue_index = 0
        elif event == "nazna":
            current_object = {"dialogues": dialogue_nazna()}
            is_dialogue_active = True
            current_dialogue_index = 0
        elif event == "memo":
            current_object = {"dialogues": dialogue_memo()}
            is_dialogue_active = True
            current_dialogue_index = 0
        else:
            return

    # 오브젝트 크기 설정
    original_sizes = [obj["image"].get_size() for obj in objects]
    small_sizes = [(int(size[0] * 0.8), int(size[1] * 0.8)) for size in original_sizes]  # 90% 크기
    transition_to_next_stage = False  # 다음 스테이지로 전환 여부

    # 게임 루프
    running = True
    while running:
        screen.blit(background, (0, 0))  # 배경 그리기

        mouse_pos = pygame.mouse.get_pos()  # 마우스 위치

        for i, obj in enumerate(objects):
            obj_image = obj["image"]
            obj_rect = obj_image.get_rect(topleft=obj["pos"])

            # 마우스가 오브젝트 위에 있으면 작아진 이미지로 그리기
            if obj_rect.collidepoint(mouse_pos):
                resized_image = pygame.transform.scale(obj_image, small_sizes[i])
                resized_rect = resized_image.get_rect(center=obj_rect.center)
                screen.blit(resized_image, resized_rect)
            else:
                screen.blit(obj_image, obj_rect)  # 원래 크기로 그리기

            # 대화창 표시
        if is_dialogue_active and current_object is not None:
            dialogue_info = current_object["dialogues"][current_dialogue_index]

            # 대화창 그리기 (상단으로 이동)
            screen.blit(dialogue_box_image, (0, 0))  # 대화창 상단에 그리기

            # 이름 출력 (상단으로 이동)
            name_text = font.render(dialogue_info["name"], True, (255, 255, 255))
            screen.blit(name_text, (228, 51))  # 이름을 화면 상단에 배치

            # 초상화 출력 (상단으로 이동)
            if "portrait" in dialogue_info:
                portrait_image = pygame.image.load(
                    os.path.join('assets', 'images', 'portrait', 'cha', dialogue_info["portrait"]))
            else:
                portrait_image = None

            if portrait_image:
                screen.blit(portrait_image, (6, 16))

            dialogue_text = font.render(dialogue_info["dialogue"], True, (255, 255, 255))

            screen.blit(dialogue_text, (240, 110))  # 대사 텍스트 상단에 배치
        # 비밀번호 입력창 표시
        if password_input_active:
            draw_password_input(screen, font2, user_input, input_active_color, input_inactive_color,
                                password_input_active)
            input_text = font2.render("비밀번호 입력: ", True, (0, 100, 200))
            screen.blit(input_text, (70, 210))  # 입력창 위치 설정

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse Clicked at {mouse_pos}")
                for obj in objects:
                    obj_rect = obj["image"].get_rect(topleft=obj["pos"])
                    if obj_rect.collidepoint(mouse_pos):
                        print(f"Object '{obj['event']}' clicked")
                        handle_object_click(obj["event"])

                # 키보드 입력 처리 (비밀번호 입력)
            elif event.type == pygame.KEYDOWN:
                if password_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]  # 입력 지우기
                    elif event.key == pygame.K_RETURN:
                        # 비밀번호 확인
                        if user_input == correct_password:
                            current_object = {"dialogues": [{"name": "차준영", "portrait": "sup.png",
                                                             "dialogue": "!!!"},
                                                            ]}
                            is_dialogue_active = True
                            current_dialogue_index = 0
                            password_input_active = False  # 비밀번호 입력 종료
                            transition_to_next_stage = True  # 대화 후 다음 스테이지 전환
                        else:
                            password_input_active = False  # 입력 종료 후 대사창에 오류 메시지 표시
                            current_object = {"dialogues": [{"name": "", "dialogue": "아무일도 일어나지 않았다."},
                                                            {"name": "차준영", "portrait": "default.png", "dialogue": "틀린 것 같아, 단서를 찾아보자"}
                                                            ]}
                            is_dialogue_active = True
                            current_dialogue_index = 0
                    else:
                        user_input += event.unicode  # 입력된 키 추가

                    # 스페이스바를 눌러 대화 진행
                elif event.key == pygame.K_SPACE and is_dialogue_active and current_object is not None:
                    current_dialogue_index += 1  # 다음 대화로 넘어감

                    # 모든 대화를 출력한 경우 대화 종료
                    if current_dialogue_index >= len(current_object["dialogues"]):
                        is_dialogue_active = False  # 대화창 비활성화
                        current_object = None  # 현재 오브젝트 초기화
                    if transition_to_next_stage:
                        running = False  # 게임 루프 종료 후 스테이지 전환

        pygame.display.update()

    stage_2_intro(screen)

