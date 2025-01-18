import pygame
import random
import math

pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
skorost = 100
radioos = 10
kolichestvo = 20
FPS = 120
GAME_DURATION = 120
TRAIL_LENGTH = 10

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncing Balls")


class Ball:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = pygame.Vector2(math.cos(self.angle), math.sin(self.angle)) * skorost / FPS

    def moov(self):
        self.pos += self.speed
        if self.pos.x - radioos <= 0 or self.pos.x + radioos >= WINDOW_WIDTH:
            self.speed.x = -self.speed.x
            self.pos.x = max(radioos, min(self.pos.x, WINDOW_WIDTH - radioos))
        if self.pos.y - radioos <= 0 or self.pos.y + radioos >= WINDOW_HEIGHT:
            self.speed.y = -self.speed.y
            self.pos.y = max(radioos, min(self.pos.y, WINDOW_HEIGHT - radioos))

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.pos.x), int(self.pos.y)), radioos)

    def check_collision(self, other):
        distance = self.pos.distance_to(other.pos)
        if distance < radioos * 2:
            self.speed, other.speed = other.speed, self.speed


def is_position_valid(x, y, balls):
    for ball in balls:
        if pygame.Vector2(x, y).distance_to(ball.pos) < 2 * radioos:
            return False
    return True


balls = []
while len(balls) < kolichestvo:
    x = random.randint(radioos, WINDOW_WIDTH - radioos)
    y = random.randint(radioos, WINDOW_HEIGHT - radioos)
    if is_position_valid(x, y, balls):
        balls.append(Ball(x, y))

running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

trail = []
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.moov()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].check_collision(balls[j])

    mouse_pos = pygame.mouse.get_pos()
    for ball in balls:
        if ball.pos.distance_to(mouse_pos) < radioos:
            running = False

    if len(trail) < TRAIL_LENGTH:
        trail.append(mouse_pos)
    else:
        trail.pop(0)
        trail.append(mouse_pos)

    screen.fill((0, 0, 0))
    for ball in balls:
        ball.draw(screen)

    for i, pos in enumerate(trail):
        fade_color = (255, 0, 0, 255 - int((255 / TRAIL_LENGTH) * i))
        pygame.draw.circle(screen, fade_color, pos, int(5))

    pygame.display.flip()
    clock.tick(FPS)

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    if elapsed_time >= GAME_DURATION:
        running = False

pygame.quit()
