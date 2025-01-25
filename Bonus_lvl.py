import pygame
import random
import math
import subprocess
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font_size=30):
        # Исправлено: метод инициализации теперь __init__
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def before():
    pygame.init()

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("bonus lvl")

    font = pygame.font.SysFont('Arial', 30)
    sr = 50
    co = 10
    rd = 10
    time = 50

    button_s1 = Button(400, 40, 20, 20, (0, 0, 0), "^", (255, 255, 255))
    button_s2 = Button(400, 90, 20, 20, (0, 0, 0), "v", (255, 255, 255))

    button_co1 = Button(400, 140, 20, 20, (0, 0, 0), "^", (255, 255, 255))
    button_co2 = Button(400, 190, 20, 20, (0, 0, 0), "v", (255, 255, 255))

    button_rd1 = Button(400, 240, 20, 20, (0, 0, 0), "^", (255, 255, 255))
    button_rd2 = Button(400, 290, 20, 20, (0, 0, 0), "v", (255, 255, 255))

    button_time1 = Button(400, 340, 20, 20, (0, 0, 0), "^", (255, 255, 255))
    button_time2 = Button(400, 390, 20, 20, (0, 0, 0), "v", (255, 255, 255))

    button_play = Button(145, 430, 200, 50, (255, 0, 0), "Играть", (255, 255, 255))
    button_meny = Button(0, 0, 100, 25, (255, 0, 0), "В меню", (255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_meny.is_clicked(event.pos):
                    running = False
                    subprocess.Popen(["python", "meny.py"])
                if button_s1.is_clicked(event.pos):
                    if sr >= 99:
                        sr = sr
                    else:
                        sr += 1
                if button_s2.is_clicked(event.pos):
                    if sr <= 1:
                        sr = sr
                    else:
                        sr -= 1
                if button_co1.is_clicked(event.pos):
                    if co >= 99:
                        co = co
                    else:
                        co += 1
                if button_co2.is_clicked(event.pos):
                    if co <= 1:
                        co = co
                    else:
                        co -= 1

                if button_rd1.is_clicked(event.pos):
                    if rd >= 50:
                        rd = rd
                    else:
                        rd += 1
                if button_rd2.is_clicked(event.pos):
                    if rd <= 1:
                        rd = rd
                    else:
                        rd -= 1

                if button_time1.is_clicked(event.pos):
                    if time >= 99:
                        time = time
                    else:
                        time += 1
                if button_time2.is_clicked(event.pos):
                    if time <= 1:
                        time = time
                    else:
                        time -= 1
                if button_play.is_clicked(event.pos):
                    after(rd, co, sr, time)

        screen.fill((255, 255, 255))

        title = font.render("Параметры уровня", True, (255, 0, 0))
        screen.blit(title, (140, 0))

        title = font.render("Скорость препятствий", True, (0, 0, 0))
        screen.blit(title, (50, 55))
        title = font.render("Количество препятствий", True, (0, 0, 0))
        screen.blit(title, (50, 155))
        title = font.render("Размер препятствий", True, (0, 0, 0))
        screen.blit(title, (50, 255))
        title = font.render("Время игры", True, (0, 0, 0))
        screen.blit(title, (50, 355))

        button_s1.draw(screen)
        text_sr = font.render(str(sr), True, (0, 0, 0))
        if sr <= 9:
            screen.blit(text_sr, (403, 56))
        if sr >= 10:
            screen.blit(text_sr, (397, 56))
        button_s2.draw(screen)

        button_co1.draw(screen)
        # Смещаем позицию для text_co, чтобы он не перекрывал text_sr
        text_co = font.render(str(co), True, (0, 0, 0))
        if co <= 9:
            screen.blit(text_co, (403, 156))  # Заменили 56 на 156 для co
        if co >= 10:
            screen.blit(text_co, (397, 156))  # Заменили 56 на 156 для co
        button_co2.draw(screen)


        button_rd1.draw(screen)
        text_rd = font.render(str(rd), True, (0, 0, 0))
        if rd <= 9:
            screen.blit(text_rd, (403, 256))  # Заменили 56 на 156 для rd
        if rd >= 10:
            screen.blit(text_rd, (397, 256))
        button_rd2.draw(screen)


        button_time1.draw(screen)
        text_time = font.render(str(time), True, (0, 0, 0))
        if time <= 9:
            screen.blit(text_time, (403, 356))  # Заменили 56 на 156 для time
        if time >= 10:
            screen.blit(text_time, (397, 356))
        button_time2.draw(screen)

        button_play.draw(screen)
        button_meny.draw(screen)
        pygame.display.update()




    pygame.quit()


def after(BALL_RADIUS, BALL_COUNT, BALL_SPEED, GAME_DURATION):
    import pygame
    import random
    import math

    pygame.init()
    a,b = random.randint(0, 255), random.randint(0, 255)
    # Constants
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    BALL_RADIUS = BALL_RADIUS
    BALL_COUNT = BALL_COUNT
    BALL_SPEED = BALL_SPEED  # Pixels per second
    FPS = 120
    GAME_DURATION = GAME_DURATION  # in seconds
    TRAIL_LENGTH = 10

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Bonus Level")
    font = pygame.font.Font(None, 36)
    background_color = (30, 30, 40)

    class Ball:
        def __init__(self, x, y):
            self.pos = pygame.Vector2(x, y)
            self.angle = random.uniform(0, 2 * math.pi)
            self.speed = pygame.Vector2(math.cos(self.angle), math.sin(self.angle)) * BALL_SPEED / FPS
            self.color = [random.randint(50, 255) for _ in range(3)]

        def move(self):
            self.pos += self.speed
            if self.pos.x - BALL_RADIUS <= 0 or self.pos.x + BALL_RADIUS >= WINDOW_WIDTH:
                self.speed.x = -self.speed.x
                self.pos.x = max(BALL_RADIUS, min(self.pos.x, WINDOW_WIDTH - BALL_RADIUS))
            if self.pos.y - BALL_RADIUS <= 0 or self.pos.y + BALL_RADIUS >= WINDOW_HEIGHT:
                self.speed.y = -self.speed.y
                self.pos.y = max(BALL_RADIUS, min(self.pos.y, WINDOW_HEIGHT - BALL_RADIUS))

        def draw(self, surface):
            pygame.draw.circle(surface, self.color, (int(self.pos.x), int(self.pos.y)), BALL_RADIUS)

        def check_collision(self, other):
            distance = self.pos.distance_to(other.pos)
            if distance < BALL_RADIUS * 2:
                self.speed, other.speed = other.speed, self.speed
                self.color = [random.randint(50, 255) for _ in range(3)]
                other.color = [random.randint(50, 255) for _ in range(3)]

    def is_position_valid(x, y, balls):
        for ball in balls:
            if pygame.Vector2(x, y).distance_to(ball.pos) < 2 * BALL_RADIUS:
                return False
        return True

    # Create balls
    balls = []
    while len(balls) < BALL_COUNT:
        x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
        y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)
        if is_position_valid(x, y, balls):
            balls.append(Ball(x, y))

    running = True
    paused = False
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    elapsed_game_time = 0  # Game time accounting for pause
    trail = []
    pygame.mouse.set_visible(False)

    # Placeholder for a Pause button class
    class PauseButton:
        def __init__(self, x, y, width, height, text, alpha=255):
            self.rect = pygame.Rect(x, y, width, height)

            self.text = text
            self.font = pygame.font.Font(None, 24)
            self.is_clicked = False
            self.alpha = alpha

        def draw(self, surface):

            button_surface = pygame.Surface((self.rect.width, self.rect.height))

            button_surface.set_alpha(self.alpha)

            if self.is_hovered():
                button_surface.set_alpha(self.alpha)

            surface.blit(button_surface, self.rect.topleft)

            text_surface = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

        def is_hovered(self):
            mouse_pos = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_pos)

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return True
            return False
    # Create pause button
    pause_button = PauseButton(460, 0, 40, 40, "| |", alpha=0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pause_button.handle_event(event):
                paused = not paused
                pygame.mouse.set_visible(paused)

        if not paused:
            current_time = pygame.time.get_ticks()
            elapsed_game_time += (current_time - start_time) / 1000.0
            start_time = current_time  # Reset start time

            for ball in balls:
                ball.move()
            for i in range(len(balls)):
                for j in range(i + 1, len(balls)):
                    balls[i].check_collision(balls[j])

            mouse_pos = pygame.mouse.get_pos()
            for ball in balls:
                if ball.pos.distance_to(mouse_pos) < BALL_RADIUS:
                    running = False
                    proigral(BALL_RADIUS, BALL_COUNT, BALL_SPEED, GAME_DURATION)

        screen.fill(background_color)
        for ball in balls:
            ball.draw(screen)

        # Mouse trail
        if len(trail) < TRAIL_LENGTH:
            trail.append(mouse_pos)
        else:
            trail.pop(0)
            trail.append(mouse_pos)

        for i, pos in enumerate(trail):
            fade_color = (255 - int((255 / TRAIL_LENGTH) * i), a, b)
            pygame.draw.circle(screen, fade_color, pos, int(5))

        remaining_time = max(0.0, GAME_DURATION - elapsed_game_time)
        timer_text = font.render(f"Time: {int(remaining_time)}s", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))
        pause_button.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def proigral(BALL_RADIUS, BALL_COUNT, BALL_SPEED, GAME_DURATION):
    pygame.init()

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Повторить?")
    button_play = Button(130, 250, 250, 50, (255, 0, 0), "Повторить?", (255, 255, 255))
    button_restart = Button(130, 350, 250, 50, (255, 0, 0), "Поменять параметры?", (255, 255, 255))

    font = pygame.font.SysFont('Arial', 50)  # Создаем шрифт Arial размером 36
    text_color = (255, 0, 0)  # Красный цвет для текста
    text_surface = font.render('Ты проиграл!', True, text_color)

    running = True
    pygame.mouse.set_visible(True)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.is_clicked(event.pos):
                    after(BALL_RADIUS, BALL_COUNT, BALL_SPEED, GAME_DURATION)
                if button_restart.is_clicked(event.pos):
                    before()

        screen.fill((0, 0, 0))

        button_play.draw(screen)
        button_restart.draw(screen)
        screen.blit(text_surface, (130, 100))


        pygame.display.update()
    pygame.quit()
before()