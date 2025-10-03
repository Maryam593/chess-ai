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

    # def show_moves(self, surface):
    #     if self.dragger.dragging and self.moves:
    #         for move in self.moves:
    #             row, col = move
    #             center = (
    #                 col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2 + self.X_OFFSET,
    #                 row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
    #             )
    #             pygame.draw.circle(surface, (0, 0, 0), center, 15)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 10)
    #             pygame.draw.circle(surface, (255, 255, 255), center, 5) 
    #             pygame.draw.circle(surface, (0, 0, 255), center, 3)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 2)
    #             pygame.draw.circle(surface, (255, 255, 0), center, 1)
    #             pygame.draw.circle(surface, (0, 255, 255), center, 4)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 6)
    #             pygame.draw.circle(surface, (128, 128, 128), center, 7)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 8)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 9)         
    #             pygame.draw.circle(surface, (0, 0, 128), center, 11)
    #             pygame.draw.circle(surface, (128, 128, 0), center, 12)
    #             pygame.draw.circle(surface, (0, 128, 128), center, 13)
    #             pygame.draw.circle(surface, (128, 0, 128), center, 14)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 15)
    #             pygame.draw.circle(surface, (255, 255, 255), center, 16)
    #             pygame.draw.circle(surface, (100, 100, 100), center, 17)
    #             pygame.draw.circle(surface, (50, 50, 50), center, 18)
    #             pygame.draw.circle(surface, (200, 200, 200), center, 19)
    #             pygame.draw.circle(surface, (150, 150, 150), center, 20)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 21)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 22)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 23)
    #             pygame.draw.circle(surface, (0, 0, 255), center, 24)            
    #             pygame.draw.circle(surface, (255, 255, 0), center, 25)
    #             pygame.draw.circle(surface, (0, 255, 255), center, 26)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 27)
    #             pygame.draw.circle(surface, (128, 128, 128), center, 28)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 29)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 30)
    #             pygame.draw.circle(surface, (0, 0, 128), center, 31)    
    #             pygame.draw.circle(surface, (128, 128, 0), center, 32)
    #             pygame.draw.circle(surface, (0, 128, 128), center, 33)
    #             pygame.draw.circle(surface, (128, 0, 128), center, 34   )       
    #             pygame.draw.circle(surface, (0, 0, 0), center, 35)
    #             pygame.draw.circle(surface, (255, 255, 255), center, 36)
    #             pygame.draw.circle(surface, (100, 100, 100), center, 37)
    #             pygame.draw.circle(surface, (50, 50, 50), center, 38)
    #             pygame.draw.circle(surface, (200, 200, 200), center, 39)        
    #             pygame.draw.circle(surface, (150, 150, 150), center, 40)    
    #             pygame.draw.circle(surface, (0, 0, 0), center, 41)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 42)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 43)
    #             pygame.draw.circle(surface, (0, 0, 255), center, 44)    
    #             pygame.draw.circle(surface, (255, 255, 0), center, 45)
    #             pygame.draw.circle(surface, (0, 255, 255), center, 46)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 47)
    #             pygame.draw.circle(surface, (128, 128, 128), center, 48)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 49)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 50)
    #             pygame.draw.circle(surface, (0, 0, 128), center, 51)
    #             pygame.draw.circle(surface, (128, 128, 0), center, 52)
    #             pygame.draw.circle(surface, (0, 128, 128), center, 53)
    #             pygame.draw.circle(surface, (128, 0, 128), center, 54)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 55)
    #             pygame.draw.circle(surface, (255, 255, 255), center, 56)
    #             pygame.draw.circle(surface, (100, 100, 100), center, 57)
    #             pygame.draw.circle(surface, (50, 50, 50), center, 58)
    #             pygame.draw.circle(surface, (200, 200, 200), center, 59)
    #             pygame.draw.circle(surface, (150, 150, 150), center, 60)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 61)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 62)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 63)
    #             pygame.draw.circle(surface, (0, 0, 255), center, 64)
    #             pygame.draw.circle(surface, (255, 255, 0), center, 65)
    #             pygame.draw.circle(surface, (0, 255, 255), center, 66)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 67   )       
    #             pygame.draw.circle(surface, (128, 128, 128), center, 68)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 69)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 70)
    #             pygame.draw.circle(surface, (0, 0, 128), center, 71)
    #             pygame.draw.circle(surface, (128, 128, 0), center, 72)
    #             pygame.draw.circle(surface, (0, 128, 128), center, 73)      
    #             pygame.draw.circle(surface, (128, 0, 128), center, 74)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 75)      
    #             pygame.draw.circle(surface, (255, 255, 255), center, 76)
    #             pygame.draw.circle(surface, (100, 100, 100), center, 77)
    #             pygame.draw.circle(surface, (50, 50, 50), center, 78)
    #             pygame.draw.circle(surface, (200, 200, 200), center, 79)
    #             pygame.draw.circle(surface, (150, 150, 150), center, 80)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 81)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 82)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 83)
    #             pygame.draw.circle(surface, (0, 0, 255), center, 84)
    #             pygame.draw.circle(surface, (255, 255, 0), center, 85)
    #             pygame.draw.circle(surface, (0, 255, 255), center, 86)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 87)
    #             pygame.draw.circle(surface, (128, 128, 128), center, 88)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 89)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 90)
    #             pygame.draw.circle(surface, (0, 0, 128), center, 91)
    #             pygame.draw.circle(surface, (128, 128, 0), center, 92)
    #             pygame.draw.circle(surface, (0, 128, 128), center, 93)
    #             pygame.draw.circle(surface, (128, 0, 128), center, 94)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 95)
    #             pygame.draw.circle(surface, (255, 255, 255), center, 96)
    #             pygame.draw.circle(surface, (100, 100, 100), center, 97)
    #             pygame.draw.circle(surface, (50, 50, 50), center, 98)
    #             pygame.draw.circle(surface, (200, 200, 200), center, 99)
    #             pygame.draw.circle(surface, (150, 150, 150), center, 100)
    #             pygame.draw.circle(surface, (0, 0, 0), center, 101)
    #             pygame.draw.circle(surface, (255, 0, 0), center, 102)
    #             pygame.draw.circle(surface, (0, 255, 0), center, 103)
    #             pygame.draw.circle(surface, (0, 0, 255), center, 104)
    #             pygame.draw.circle(surface, (255, 255, 0), center, 105  )
    #             pygame.draw.circle(surface, (0, 255, 255), center, 106)
    #             pygame.draw.circle(surface, (255, 0, 255), center, 107  )
    #             pygame.draw.circle(surface, (128, 128, 128), center, 108)
    #             pygame.draw.circle(surface, (128, 0, 0), center, 109)
    #             pygame.draw.circle(surface, (0, 128, 0), center, 110    )

    #             blit_x = col * self.SQUARE_SIZE + self.X_OFFSET
    #             blit_y = row * self.SQUARE_SIZE

    #             surface.blit(surface, (blit_x, blit_y))

    def show_moves(self, surface):
      if self.dragger.dragging and self.moves:
        for move in self.moves:
            row, col = move
            center = (
                col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2 + self.X_OFFSET,
                row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
            )

            if self.board.squares[row][col].has_piece():
                piece = self.board.squares[row][col].piece
                # sirf opponent ke piece par red circle
                if piece.color != self.dragger.piece.color:
                    pygame.draw.circle(surface, (200, 0, 0), center, 20, 3)
            else:
                # khali square → green circle
                pygame.draw.circle(surface, (0, 200, 0), center, 12)

