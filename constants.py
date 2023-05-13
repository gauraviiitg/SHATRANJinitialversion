import pygame

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
BROWN = (139, 69, 19)
LIGHT_BROWN = (205, 133, 63)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('C:/Users/ASUS/Documents/WB Games/py/Python-Checkers/checkers/assets/crown.png'), (44, 25))

# Change the color values of RED, BLACK, and BLUE:
RED = BLACK
BLACK = LIGHT_BROWN
BLUE = RED
