import pygame

class Model1Verbose:
    def __init__(self):
        # Font initialization
        self.font_title = pygame.font.SysFont(None, 28)
        self.font_text = pygame.font.SysFont(None, 22)

    def show_bg(self, surface, game_state=None):
        # Colors
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)

        y_offset = 10

        # Title
        title = "White Player"
        title_surface = self.font_title.render(title, True, WHITE)
        surface.blit(title_surface, (10, y_offset))
        y_offset += 35

        if game_state:
            # Show status
            if game_state['current_turn'] == 'white':
                if game_state['dragging']:
                    status = "Thinking..."
                    color = YELLOW
                    piece_info = f"Moving: {game_state['dragging_piece']}"
                else:
                    status = "Your Turn"
                    color = GREEN
                    piece_info = ""
            else:
                status = "Waiting..."
                color = WHITE
                piece_info = ""

            status_surface = self.font_text.render(status, True, color)
            surface.blit(status_surface, (10, y_offset))
            y_offset += 25

            if piece_info:
                piece_surface = self.font_text.render(piece_info, True, WHITE)
                surface.blit(piece_surface, (10, y_offset))
                y_offset += 25

            # Show last move
            if game_state.get('last_move'):
                y_offset += 10
                last_move_text = "Last Move:"
                last_surface = self.font_text.render(last_move_text, True, WHITE)
                surface.blit(last_surface, (10, y_offset))
                y_offset += 20

                move_surface = self.font_text.render(game_state['last_move'], True, WHITE)
                surface.blit(move_surface, (10, y_offset))