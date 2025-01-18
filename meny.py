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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифты
font = pygame.font.SysFont('Arial', 30)

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
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

# Функции действий
def start_level_1():
    print("Запуск уровня 1")
    subprocess.Popen(["python", "Level 1.py"])  # Запуск level_1.py

def go_back():
    global current_screen
    current_screen = 'main_menu'

def level_select_screen():
    global current_screen
    current_screen = 'level_select'

# Главное меню
def main_menu():
    global current_screen
    buttons = [
        Button(150, 100, 200, 50, "Играть", level_select_screen),
    ]

    while current_screen == 'main_menu':
        screen.fill(WHITE)

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

        pygame.display.flip()

# Экран выбора уровня
def level_select_menu():
    global current_level, current_screen

    # Равномерное расположение кнопок для уровня
    level_buttons = [
        Button(150, 150, 200, 50, "Уровень 1", start_level_1),
        Button(150, 220, 200, 50, "Уровень 2", None),  # Заглушка для уровня 2
        Button(150, 290, 200, 50, "Уровень 3", None),  # Заглушка для уровня 3
    ]
    
    # Кнопка назад размещается ниже всех кнопок
    back_button = Button(150, 400, 200, 50, "Назад", go_back)

    while current_screen == 'level_select':
        screen.fill(WHITE)

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

        pygame.display.flip()

# Главный цикл
if __name__ == "__main__":
    current_screen = 'main_menu'
    while True:
        if current_screen == 'main_menu':
            main_menu()
        elif current_screen == 'level_select':
            level_select_menu()
