import pygame
import math
import random

pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
skorost = 100
radioos = 10
kolichestvo = 20
FPS = 120
GAME_DURATION = 120
TRAIL_LENGTH = 10

background_color = (30, 30, 40)
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncing Balls")


class Ball:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = pygame.Vector2(math.cos(self.angle), math.sin(self.angle)) * skorost / FPS
        self.color = [random.randint(50, 255) for _ in range(3)]

    def move(self):
        self.pos += self.speed
        if self.pos.x - radioos <= 0 or self.pos.x + radioos >= WINDOW_WIDTH:
            self.speed.x = -self.speed.x
            self.pos.x = max(radioos, min(self.pos.x, WINDOW_WIDTH - radioos))
        if self.pos.y - radioos <= 0 or self.pos.y + radioos >= WINDOW_HEIGHT:
            self.speed.y = -self.speed.y
            self.pos.y = max(radioos, min(self.pos.y, WINDOW_HEIGHT - radioos))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos.x), int(self.pos.y)), radioos)

    def check_collision(self, other):
        distance = self.pos.distance_to(other.pos)
        if distance < radioos * 2:
            self.speed, other.speed = other.speed, self.speed
            self.color = [random.randint(50, 255) for _ in range(3)]
            other.color = [random.randint(50, 255) for _ in range(3)]


def is_position_valid(x, y, balls):
    for ball in balls:
        if pygame.Vector2(x, y).distance_to(ball.pos) < 2 * radioos:
            return False
    return True


class Button:
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

a,b = random.randint(0, 255), random.randint(0, 255)
balls = []
while len(balls) < kolichestvo:
    x = random.randint(radioos, WINDOW_WIDTH - radioos)
    y = random.randint(radioos, WINDOW_HEIGHT - radioos)
    if is_position_valid(x, y, balls):
        balls.append(Ball(x, y))

running = True
paused = False
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
elapsed_game_time = 0  # Время игры с учетом паузы

trail = []
pygame.mouse.set_visible(False)

# Создание кнопки паузы
pause_button = Button(460, 0, 40, 40, "| |",alpha=0)

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

        for ball in balls:
            ball.move()

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].check_collision(balls[j])

        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            if ball.pos.distance_to(mouse_pos) < radioos:
                running = False


    screen.fill(background_color)
    for ball in balls:
        ball.draw(screen)

    # След мыши с затуханием
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

    # Обновляем стартовое время только если игра не на паузе
    start_time = current_time if not paused else start_time

    clock.tick(FPS)

pygame.quit()
