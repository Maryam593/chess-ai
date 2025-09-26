import pygame
import sys
from board import Board
from game import Game
from const import * # Assuming WIDTH, HEIGHT, aur BOARD_WIDTH yahan defined hain
from verbose1 import Model1Verbose
from verbose2 import Model2Verbose


class Main:
    def __init__(self):
        # 1. Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.clock = pygame.time.Clock()
        
        # 2. Game aur Verbose Objects
        self.game = Game()
        self.verbose1 = Model1Verbose()
        self.verbose2 = Model2Verbose()
        
        # NOTE: self.game.show_bg(self.screen) ko __init__ se hata diya hai.
        # Isko sirf mainloop mein hona chahiye taake har frame mein draw ho.

    def mainloop(self):
        screen = self.screen
        game = self.game
        verbose1 = self.verbose1
        verbose2 = self.verbose2
        
        # Ek default background color for the side panels' area
        # Grey ya halka black behtar hai taake text nazar aaye
        BG_COLOR = (40, 40, 40) 
        
        while True:
            
            # --- Drawing Order ---
            
            # 1. Screen ki safai (Puri screen ko saaf karein)
            screen.fill(BG_COLOR) 
            
            # 2. Chess Board Draw karein (Beech mein)
            # Zaroori hai ki game.py mein X_OFFSET use ho raha ho
            game.show_bg(screen) 
            
            # 3. Verbose 1 Draw karein (Left Side Panel)
            verbose1.show_bg(screen)
            
            # 4. Verbose 2 Draw karein (Right Side Panel)
            verbose2.show_bg(screen)

            #5. Pieces Draw karein (Board ke upar)
            game.show_pieces(screen,self.game.board)

            # --- Event Handling ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Update Display ---
            pygame.display.update()
            self.clock.tick(60) # Frame rate set karna achha hai


main = Main()
main.mainloop()