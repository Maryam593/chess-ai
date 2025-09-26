import pygame

class Model1Verbose:
    def __init__(self):
        # Font initialization
        self.font = pygame.font.SysFont(None, 24)
        
    def show_bg(self, surface):
        # Colors
        # BLACK = (0, 0, 0) # Hata diya gaya hai taaki yeh poori screen ko overwrite na kare
        WHITE = (255, 255, 255)
        
        # Text rendering
        text_content = "Model 1 Verbose"
        text_surface = self.font.render(text_content, True, WHITE)
        text_rect = text_surface.get_rect()
        
        # Position Set Karna (Left Side Top)
        # top: 10 pixels neechay, left: 10 pixels left edge se door
        text_rect.topleft = (10, 10) 
        
        # Text ko screen par draw karein
        surface.blit(text_surface, text_rect)