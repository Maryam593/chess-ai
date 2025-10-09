import pygame

class Model2Verbose:
    def __init__(self):
        self.font_title = pygame.font.SysFont(None, 28)
        self.font_text = pygame.font.SysFont(None, 22)

    def show_bg(self, surface, game_state=None):
        # Colors
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)

        screen_width = surface.get_width()
        y_offset = 10

        # Title
        title = "Black Player"
        title_surface = self.font_title.render(title, True, WHITE)
        title_rect = title_surface.get_rect()
        title_rect.topright = (screen_width - 10, y_offset)
        surface.blit(title_surface, title_rect)
        y_offset += 35

        if game_state:
            # Show status
            if game_state['current_turn'] == 'black':
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
            status_rect = status_surface.get_rect()
            status_rect.topright = (screen_width - 10, y_offset)
            surface.blit(status_surface, status_rect)
            y_offset += 25

            if piece_info:
                piece_surface = self.font_text.render(piece_info, True, WHITE)
                piece_rect = piece_surface.get_rect()
                piece_rect.topright = (screen_width - 10, y_offset)
                surface.blit(piece_surface, piece_rect)
                y_offset += 25

            # # Show last move
            # if game_state.get('last_move'):
            #     y_offset += 10
            #     last_move_text = "Last Move:"
            #     last_surface = self.font_text.render(last_move_text, True, WHITE)
            #     last_rect = last_surface.get_rect()
            #     last_rect.topright = (screen_width - 10, y_offset)
            #     surface.blit(last_surface, last_rect)
            #     y_offset += 20

            #     move_surface = self.font_text.render(game_state['last_move'], True, WHITE)
            #     move_rect = move_surface.get_rect()
            #     move_rect.topright = (screen_width - 10, y_offset)
            #     surface.blit(move_surface, move_rect)