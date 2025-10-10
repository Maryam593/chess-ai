# game.py

import pygame
from const import *
from board import Board
from dragger import Dragger 
from verbose1 import Model1Verbose
from verbose2 import Model2Verbose
from theme import Theme
from config import Config

class Game:
    def __init__ (self):
        self.board = Board()
        self.dragger = Dragger()
        self.verbose1 = Model1Verbose()
        self.verbose2 = Model2Verbose()
        self.SQUARE_SIZE = SQUARE_SIZE
        self.hovered_sqr = None # Stores the Square object that is currently hovered
        self.config = Config()  # Theme configuration
        self.theme = self.config.themes
        self.X_OFFSET = (WIDTH - BOARD_WIDTH) // 2
        self.ROWS = ROWs
        self.COLS = COLs
        self.next_player = 'white'  # Track whose turn it is
        self.moves = []  # Initialize moves list
        self.last_move_info = None  # Track last move for display

    def show_bg(self, surface):
        theme = self.config.themes
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                #color
                color = theme.bg.light if (row+col) % 2 == 0 else theme.bg.dark
                # rect 
                rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                rect_y = row * self.SQUARE_SIZE
                #blit
                pygame.draw.rect(surface, color, (rect_x, rect_y, self.SQUARE_SIZE, self.SQUARE_SIZE))
    
    def show_last_move(self, surface):
        theme = self.config.themes
        if self.board.last_move:
            start_pos_tuple = self.board.last_move.start_pos
            end_pos_tuple = self.board.last_move.end_pos
            
            for row, col in [start_pos_tuple, end_pos_tuple]:
                
                LIGHT = (246, 246, 105) 
                DARK = (186, 202, 43)   

                # Calculate highlight color based on original square color
                color = theme.trace.light if (row + col) % 2 == 0 else theme.trace.dark
                
                rect_x = self.X_OFFSET + col * self.SQUARE_SIZE
                rect_y = row * self.SQUARE_SIZE
                
                pygame.draw.rect(surface, color, (rect_x, rect_y, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180, 150) # Use RGBA for slight transparency (requires surface support)
            
            # Recalculate rect using the hovered square's attributes and the X_OFFSET
            rect_x = self.X_OFFSET + self.hovered_sqr.col * self.SQUARE_SIZE
            rect_y = self.hovered_sqr.row * self.SQUARE_SIZE
            
            # Blit the highlight
            s = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE), pygame.SRCALPHA)
            s.fill(color)
            surface.blit(s, (rect_x, rect_y))

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
        # 1. CRITICAL CHECK: If no piece is being dragged or there are no moves, exit immediately.
        if not self.dragger.dragging or not self.dragger.piece or not self.moves:
            return

        # 2. THEME ACCESS: Use the correct variable name (assuming Config uses 'current_theme')
        theme = self.config.themes
        
        # 3. COLOR CALCULATION (Now Safe): Calculate the color only when a piece is present.
        #    Also use .value to get the RGB tuple from your Color object.
        if self.dragger.piece.color == 'white':
            thColor = theme.moves.light
        else:
            thColor = theme.moves.dark

        # The rest of the logic remains inside the loop
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
                # khali square → use the calculated thColor
                pygame.draw.circle(surface, thColor, center, 12)

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
    
    def reset(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.moves = []
        self.last_move_info = None
        self.hovered_sqr = None
    
    def sound_effect(self, capture=False):
        if capture:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
    
    def change_theme(self):
        self.config.change_theme()
        print(f"Theme changed to: {self.config.themes.name}")    

    def set_hover(self, row, col):
        """Sets the hovered square or clears it if coordinates are out of bounds."""
        if 0 <= row < self.ROWS and 0 <= col < self.COLS:
            self.hovered_sqr = self.board.squares[row][col]
        else:
            self.hovered_sqr = None # Clear hover state if off-board

    def get_game_state(self):
        # Build game state dict for verbose panels
        state = {
            'current_turn': self.next_player,
            'dragging': self.dragger.dragging,
            'dragging_piece': self.dragger.piece.name if self.dragger.piece else None,
            'last_move': self.last_move_info
        }
        return state
