import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 700                               
WIN = pygame.display.set_mode((WIDTH, HEIGHT))          
pygame.display.set_caption("Rain Dodge")

BG = pygame.transform.scale(pygame.image.load("assets/bg.jpeg"), (WIDTH, HEIGHT))

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20 
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)
TITLE_FONT = pygame.font.SysFont("comicsans", 60)
BUTTON_FONT = pygame.font.SysFont("comicsans", 40)