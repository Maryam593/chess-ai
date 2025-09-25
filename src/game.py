import pygame
from const import *
import sys

class Game:
    def __init__(self):
        print("game initialized")

    # def reset(self):
    #     print("game reset")

    def show_bg(self, surface):
        print("show background")
        for row in range(ROWs):
            for col in range(COLs):
                if (row + col) % 2 == 0:
                    color = (235, 235, 208)  # light square
                else:
                    color = (119, 148, 85)   # dark square
                pygame.draw.rect(
                    surface,
                    color,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )
