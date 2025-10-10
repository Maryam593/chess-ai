import pygame
import sys
from game import Game
from const import * # WIDTH, HEIGHT, SQUARE_SIZE etc.
import move
from verbose1 import Model1Verbose
from verbose2 import Model2Verbose


class Main:
    def __init__(self):
        # 1. Initialization
        pygame.init()
        # Ensure the screen supports transparency for hover effect
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
        pygame.display.set_caption('Chess')
        self.clock = pygame.time.Clock()

        # 2. Game aur Verbose Objects
        self.game = Game()
        self.verbose1 = Model1Verbose()
        self.verbose2 = Model2Verbose()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board_obj = self.game.board
        dragger = self.game.dragger
        verbose1 = self.verbose1
        verbose2 = self.verbose2

        # Side panels background color
        BG_COLOR = (40, 40, 40)

        while True:
            # --- Drawing Order ---
            screen.fill(BG_COLOR)                  # 1. Clear screen
            game.show_bg(screen)                   # 2. Chess Board Background
            game.show_last_move(screen)            # 3. Last Move Highlight
            game.show_hover(screen)                # 4. Hover Highlight (NEWLY ADDED TO DRAWING LOOP)

            # Get game state for verbose panels
            game_state = game.get_game_state()
            verbose1.show_bg(screen, game_state)   # 5. Left panel (White)
            verbose2.show_bg(screen, game_state)   # 6. Right panel (Black)

            game.show_pieces(screen, board_obj)    # 7. Pieces
            game.show_moves(screen)
            if dragger.dragging:
                dragger.update_blit(screen)        # 8. Dragging piece

            # --- Event Handling ---
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    # ✅ Correct mapping (Y = row, X = col)
                    clicked_row =( dragger.mouseY - Y_OFFSET) // SQUARE_SIZE
                    clicked_col = (dragger.mouseX - X_OFFSET) // SQUARE_SIZE

                    # ✅ Bounds check (avoid IndexError)
                    if 0 <= clicked_row < ROWs and 0 <= clicked_col < COLs:
                        square = board_obj.squares[clicked_row][clicked_col]
                        print(f"Clicked: row={clicked_row}, col={clicked_col}, piece={square.piece}")


                        if square and square.has_piece():
                            piece = square.piece
                            # Only allow dragging if it's this piece's turn
                            if piece.color == game.next_player:
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)
                                game.moves = board_obj.calculate_moves(piece, clicked_row, clicked_col)
                            else:
                                print(f"Not {piece.color}'s turn!")
                                game.moves = []
                        else : game.moves = []  # Clear moves if empty square clicked

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #calculate destination
                        released_row = (dragger.mouseY - Y_OFFSET) // SQUARE_SIZE
                        released_col = (dragger.mouseX - X_OFFSET) // SQUARE_SIZE

                        #avoid going out of board
                        if 0 <= released_row < ROWs and 0 <= released_col < COLs:
                            piece = dragger.piece
                            start_pos = (dragger.initial_row, dragger.initial_col)
                            end_pos = (released_row, released_col)
                            move_instance = move.Move(piece, start_pos, end_pos)
                            #validate move
                            if board_obj.validate_move(piece, move_instance):
                                board_obj.move(piece, start_pos, end_pos)
                            
                                game.record_move(piece, start_pos, end_pos)  # Record for verbose
                                game.next_turn()
                                print("valid move")
                            else: print("invalid move")

                    dragger.undrag_piece()
                    game.moves = []  # Clear moves on drop

                elif event.type == pygame.MOUSEMOTION:
                    
                    motion_row = (event.pos[1] - Y_OFFSET) // SQUARE_SIZE
                    motion_col = (event.pos[0] - X_OFFSET) // SQUARE_SIZE
                    
                    # Pass coordinates to set_hover. set_hover will handle boundary checking.
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                         dragger.update_mouse(event.pos)
                         dragger.update_blit(screen)
                         # show_hover is now called in the main drawing loop

                #key_press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:    # Changing themes
                        game.change_theme()
                    if event.key == pygame.K_r:    # Reset game
                        game.reset()    
                         
                  

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            # --- Update Display ---
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    main = Main()
    main.mainloop()
