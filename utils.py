import os
import pygame

from settings import *

def load_high_score():
    if not os.path.exists("highscore.txt"):  
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        return int(f.read())


def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def draw_button(text, x, y, width, height, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    btn_rect = pygame.Rect(x, y, width, height)

    if btn_rect.collidepoint(mouse_pos):
        pygame.draw.rect(WIN, hover_color, btn_rect)
        if click:
            return True    
    else:
        pygame.draw.rect(WIN, color, btn_rect)


    btn_text = BUTTON_FONT.render(text, 1, WHITE)
    WIN.blit(btn_text, (x + (width - btn_text.get_width())//2,
                        y + (height - btn_text.get_height())//2))

    return False