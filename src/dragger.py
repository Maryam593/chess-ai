import pygame
from const import *
from square import Square
from piece import *
class Dragger:
    # def __init__(self, piece, row, col):
    #     self.piece = piece
    #     self.row = row
    #     self.col = col
    #     self.x = 0
    #     self.y = 0  
    #     self.dragging = False

    # def update_blit(self, surface):
    #     texture = pygame.image.load(self.piece.texture)
    #     texture = pygame.transform.scale(texture, (SQUARE_SIZE, SQUARE_SIZE))
    #     rect = texture.get_rect()
    #     rect.center = (self.x, self.y)
    #     surface.blit(texture, rect)
    #     pygame.draw.circle(surface, (255,0,0), (self.x, self.y), 15)
    #     pygame.draw.circle(surface, (0,255,0), (self.x, self.y), 10)
    #     pygame.draw.circle(surface, (0,0,255), (self.x, self.y), 5)
    #     pygame.draw.circle(surface, (255,255,255), (self.x, self.y), 2)
    #     pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 1)
    #     pygame.draw.circle(surface, (255,255,0), (self.x, self.y), 3)
    #     pygame.draw.circle(surface, (0,255,255), (self.x, self.y), 4)
    #     pygame.draw.circle(surface, (255,0,255), (self.x, self.y), 6)
    #     pygame.draw.circle(surface, (128,128,128), (self.x, self.y), 7)
    #     pygame.draw.circle(surface, (128,0,0), (self.x, self.y  ), 8)
    #     pygame.draw.circle(surface, (0,128,0), (self.x, self.y), 9)
    #     pygame.draw.circle(surface, (0,0,128), (self.x, self.y), 11)
    #     pygame.draw.circle(surface, (128,128,0), (self.x, self.y), 12)
    #     pygame.draw.circle(surface, (0,128,128), (self.x, self.y), 13)
    #     pygame.draw.circle(surface, (128,0,128), (self.x, self.y), 14) 
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        self.piece.set_texture(size = 80) # Resize texture to 128x128 pixels
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
    
    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)
    def save_initial(self,pos):
        self.initial_row = pos [1] // SQUARE_SIZE
        self.initial_col = pos [0] // SQUARE_SIZE 
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    def undrag_piece(self):
        self.piece = None
        self.dragging = False