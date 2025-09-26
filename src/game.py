# game.py

import pygame
from const import *
from board import Board
class Game:
    def __init__ (self): 
        self.board = Board()
        self.SQUARE_SIZE = SQUARE_SIZE
       
        self.X_OFFSET = (WIDTH - BOARD_WIDTH) // 2 
        self.ROWS = ROWs
        self.COLS = COLs

    def show_bg(self, surface):
        for row in range(self.ROWS):
            LIGHT = (234, 235, 200)
            DARK = (119, 154, 88)
            for col in range(self.COLS):
                if (row + col) % 2 == 0:
                    color = LIGHT
                else:
                    color = DARK
                
                rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                rect_y = row * self.SQUARE_SIZE
                
                pygame.draw.rect(surface, color, (rect_x, rect_y, self.SQUARE_SIZE, self.SQUARE_SIZE))
    
    def show_pieces(self, surface, board):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                piece = board.squares[row][col].piece
                if piece is not None:
                    texture = pygame.image.load(piece.texture)
                    texture = pygame.transform.scale(texture, (self.SQUARE_SIZE, self.SQUARE_SIZE))
                    rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                    rect_y = row * self.SQUARE_SIZE
                    surface.blit(texture, (rect_x, rect_y)) 
    