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
        self.next_player = 'white'  # Track whose turn it is
        self.moves = []  # Initialize moves list
        self.last_move_info = None  # Track last move for display

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
    
    def show_last_move(self, surface):
        if self.board.last_move:
            # FIX: Use the correct attribute names: start_pos and end_pos
            start_pos_tuple = self.board.last_move.start_pos
            end_pos_tuple = self.board.last_move.end_pos
            
            # Iterate over the two (row, col) tuples
            for row, col in [start_pos_tuple, end_pos_tuple]:
                
                # The rest of the logic is correct for highlighting
                LIGHT = (246, 246, 105) # Lighter highlight color
                DARK = (186, 202, 43)   # Darker highlight color

                color = LIGHT if (row + col) % 2 == 0 else DARK
                
                # Need to use the stored SQUARE_SIZE and X_OFFSET
                rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                rect_y = row * self.SQUARE_SIZE
                
                # Draw the highlight
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

    def next_turn(self):
        # Switch turns between white and black
        self.next_player = 'black' if self.next_player == 'white' else 'white'

    def record_move(self, piece, start_pos, end_pos):
        # Record move for display in verbose panels
        start_col = chr(97 + start_pos[1])  # Convert to a-h
        start_row = 8 - start_pos[0]  # Convert to 1-8
        end_col = chr(97 + end_pos[1])
        end_row = 8 - end_pos[0]
        self.last_move_info = f"{piece.name} {start_col}{start_row}-{end_col}{end_row}"

    def get_game_state(self):
        # Build game state dict for verbose panels
        state = {
            'current_turn': self.next_player,
            'dragging': self.dragger.dragging,
            'dragging_piece': self.dragger.piece.name if self.dragger.piece else None,
            'last_move': self.last_move_info
        }
        return state

