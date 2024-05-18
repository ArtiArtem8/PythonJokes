import sys

import pygame as pg
from pygame.math import *

pg.init()

# Размер окна
screen_width = 1600
screen_height = 1000
screen = pg.display.set_mode((screen_width, screen_height))

# Загружаем изображение
path = r'C:\Users\a_shi\Downloads\Telegram Desktop\14\\'
init_file = r'F_24_9_0045-0134'
image_path = init_file + '.jpg'
image = pg.image.load(path + image_path)
image_rect = image.get_rect()
image_height = image_rect.height
font = pg.font.Font(None, 5)

# Переменные для прокрутки изображения
scroll_x = 0
scroll_y = 0
scroll_speed = 50

# Цвета для точек
red = (255, 0, 0)
blue = (0, 0, 255)

# Координаты точек
left_click_point = None
right_click_point = None

# Основной цикл программы
running = True
points = []
last_char = ''

def enter():
    a = Vector2(left_click_point)
    b = Vector2(right_click_point)
    c = b - a
    points.append((last_char, int(a.x), int(a.y), int(c.x), int(c.y)))
    save(path + init_file + '.box')

def load(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            char = parts[0]
            x = int(parts[1])
            y =  int(parts[2])
            x2 = int(parts[3])
            y2 = int(parts[4])
            width = x2 - x
            height = y2 - y
            points.append((char, x, image_height - y2, width, height))
            print(points[-1])
def save(path):
    with open(path, 'w', encoding='utf-8') as file:
        for char, x, y, width, height in points:
            file.write(f"{char} {x} {image_height - y - height} {x + width} {image_height - y} 0\n")
            # print(f"{char} {x} {image_height - y - height} {x + width} {image_height - y} 0\n")

load(path + init_file + '.box')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                enter()
            last_char = event.unicode
            print(last_char)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                left_click_point = (event.pos[0] + scroll_x, event.pos[1] + scroll_y)
                print(f"Left click at: {left_click_point}")
            elif event.button == 3:  # Правая кнопка мыши
                right_click_point = (event.pos[0] + scroll_x, event.pos[1] + scroll_y)
                print(f"Right click at: {right_click_point}")
        elif event.type == pg.MOUSEWHEEL:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                scroll_x -= event.y * scroll_speed
                scroll_x = max(0, min(scroll_x, image_rect.width - screen_width))
            else:
                scroll_y -= event.y * scroll_speed
                scroll_y = max(0, min(scroll_y, image_rect.height - screen_height))

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        scroll_x = max(scroll_x - scroll_speed, 0)
    if keys[pg.K_RIGHT]:
        scroll_x = min(scroll_x + scroll_speed, image_rect.width - screen_width)
    if keys[pg.K_UP]:
        scroll_y = max(scroll_y - scroll_speed, 0)
    if keys[pg.K_DOWN]:
        scroll_y = min(scroll_y + scroll_speed, image_rect.height - screen_height)

    # Отображение изображения
    screen.fill((0, 0, 0))
    screen.blit(image, (-scroll_x, -scroll_y))

    # Отображение точек
    if left_click_point:
        pg.draw.circle(screen, red, (left_click_point[0] - scroll_x, left_click_point[1] - scroll_y), 5)
    if right_click_point:
        pg.draw.circle(screen, blue, (right_click_point[0] - scroll_x, right_click_point[1] - scroll_y), 5)
    if left_click_point and right_click_point:
        pg.draw.rect(screen, red, (left_click_point[0] - scroll_x, left_click_point[1] - scroll_y, right_click_point[0] - left_click_point[0], right_click_point[1] - left_click_point[1]), 1)
    for char, x, y, width, height in points:
        pg.draw.rect(screen, (255, 255, 255), (x - scroll_x, y - scroll_y, width, height), 1)
        text = font.render(char, True, (255, 255, 255))
        screen.blit(text, (x - scroll_x, y - scroll_y))
    # Обновление экрана
    pg.display.flip()

# Завершение работы Pygame
pg.quit()
sys.exit()