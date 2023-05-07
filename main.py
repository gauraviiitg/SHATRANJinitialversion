import pygame
pygame.font.init()
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from checkers.minimax.algorithm import minimax

FPS = 60

# Load the welcome image
WELCOME_IMAGE = pygame.image.load('C:/Users/ASUS/Documents/WB Games/py/Python-Checkers/checkers/assets/welcome.png')

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = None

    # Blit the welcome image onto the game window surface
    WIN.blit(WELCOME_IMAGE, (0, 0))
    pygame.display.update()

    # Wait for the user to press a key to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                run = False
            if event.type == pygame.KEYDOWN:
                waiting = False
                game = Game(WIN)

        clock.tick(FPS)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()
