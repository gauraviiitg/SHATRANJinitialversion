import pygame
from .constants import SQUARE_SIZE, GREY, CROWN

class Piece:
    PADDING = 5
    OUTLINE = 2
    FONT_SIZE = 35
    FONT = pygame.font.SysFont('calibri', FONT_SIZE)

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        
        if self.color == (255, 255, 255):
            label = self.FONT.render("W", 1, (0, 0, 0))
        else:
            label = self.FONT.render("B", 1, (255, 255, 255))
            
        win.blit(label, (self.x - label.get_width()//2, self.y - label.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
