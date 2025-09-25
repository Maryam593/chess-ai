import pygame
import sys
from const import *



class Main:
    def __init__(self):
        # pass
        # print('hello world')
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.clock = pygame.time.Clock()

    def mainloop(self):
        # pass
        # print('hello world')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # self.screen.fill((0, 0, 0))
            # pygame.display.flip()
            # self.clock.tick(60)

            pygame.display.update()


main = Main()
main.mainloop()
