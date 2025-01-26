import pygame
import sys
import subprocess

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Цвета
WHITE = (245, 245, 245)
BLACK = (50, 50, 50)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (70, 130, 180)

# Шрифты
font = pygame.font.SysFont('Arial', 25)

# Уровни игры
levels = ['Уровень 1', 'Уровень 2', 'Уровень 3']
current_level = 0

# Классы кнопок
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, LIGHT_BLUE, self.rect, border_radius=10)
        pygame.draw.rect(surface, DARK_BLUE, self.rect, 3, border_radius=10)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

# Функции действий
def start_level_1():
    print("Запуск уровня 1")
    subprocess.Popen(["python", "Level 1.py"])

def start_level_2():
    print("Запуск уровня 2")
    subprocess.Popen(["python", "Level 2.py"])

def start_level_3():
    print("Запуск уровня 3")
    subprocess.Popen(["python", "Level 3.py"])

def start_bonus_lvl():
    subprocess.Popen(["python", "Bonus_lvl.py"])

def go_back():
    global current_screen
    current_screen = 'main_menu'

def level_select_screen():
    global current_screen
    current_screen = 'level_select'

# Фон
def draw_background():
    for y in range(0, HEIGHT, 50):
        for x in range(0, WIDTH, 50):
            color = LIGHT_BLUE if (x // 50 + y // 50) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (x, y, 50, 50))

# Главное меню
def main_menu():
    global current_screen
    buttons = [
        Button(150, 150, 200, 50, "Играть", level_select_screen),
    ]

    while current_screen == 'main_menu':
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_hovered(pos):
                        if button.action:
                            button.action()

        # Отображение кнопок
        for button in buttons:
            button.draw(screen)

        # Заголовок
        title_surface = font.render("Главное меню", True, DARK_BLUE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 80))
        screen.blit(title_surface, title_rect)

        pygame.display.flip()

# Экран выбора уровня
def level_select_menu():
    global current_level, current_screen

    # Равномерное расположение кнопок для уровня
    level_buttons = [
        Button(150, 150, 200, 50, "Уровень 1", start_level_1),
        Button(150, 220, 200, 50, "Уровень 2", start_level_2),
        Button(150, 290, 200, 50, "Уровень 3", start_level_3),
        Button(150, 80, 200, 50, "Бонусный уровень", start_bonus_lvl)
    ]

    # Кнопка назад размещается ниже всех кнопок
    back_button = Button(150, 400, 200, 50, "Назад", go_back)

    while current_screen == 'level_select':
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in level_buttons:
                    if button.is_hovered(pos):
                        if button.action:
                            button.action()
                if back_button.is_hovered(pos):
                    go_back()

        # Отображение кнопок уровня
        for button in level_buttons:
            button.draw(screen)

        # Отображение кнопки назад
        back_button.draw(screen)

        # Заголовок
        title_surface = font.render("Выбор уровня", True, DARK_BLUE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 40))
        screen.blit(title_surface, title_rect)

        pygame.display.flip()

# Главный цикл
if __name__ == "__main__":
    current_screen = 'main_menu'
    while True:
        if current_screen == 'main_menu':
            main_menu()
        elif current_screen == 'level_select':
            level_select_menu()
