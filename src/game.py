# game.py

import pygame
from const import *
from board import Board
from dragger import Dragger 
from verbose1 import Model1Verbose
from verbose2 import Model2Verbose
class Game:
    def __init__ (self): 
        self.board = Board()
        self.dragger = Dragger()   
        self.verbose1 = Model1Verbose()
        self.verbose2 = Model2Verbose()
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
    
  
    def show_pieces(self, surface, board_obj):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board_obj.squares[row][col].has_piece():
                    piece = board_obj.squares[row][col].piece
                    if piece is self.dragger.piece and self.dragger.dragging:
                        continue

                    piece.set_texture(size=80)
                    img = pygame.image.load(piece.texture)

                    # ✅ Apply offsets
                    img_center = (
                        col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2 + self.X_OFFSET,
                        row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
                    )

                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
