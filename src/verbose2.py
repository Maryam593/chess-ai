import pygame

class Model2Verbose:
     def __init__(self):
        self.font = pygame.font.SysFont(None,24)
     def show_bg(self,surface):
        BLACK = (0,0,0)
        WHITE = (255,255,255)
      #   surface.fill(BLACK)
        text_content = "Model 2 verbose"
        text_surface = self.font.render(text_content, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topright = (surface.get_width() - 10, 10) 
        surface.blit(text_surface, text_rect)