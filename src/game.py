# game.py

import pygame
from const import *

class Game:
    # Yahan 'Self' ki jagah 'self' (small s) use karein
    def __init__ (self): 
        # Yeh Python ka standard (convention) hai
        
        # In variables ko 'self.' ke saath define karein
        self.SQUARE_SIZE = SQUARE_SIZE
        # Ensure 'WIDTH' aur 'BOARD_WIDTH' const.py se import ho rahe hon
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
                
                # Ab yeh variables 'self' object mein mil jayenge
                rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                rect_y = row * self.SQUARE_SIZE
                
                # Draw rect call bhi theek hona chahiye
                pygame.draw.rect(surface, color, (rect_x, rect_y, self.SQUARE_SIZE, self.SQUARE_SIZE))