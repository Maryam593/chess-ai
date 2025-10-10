import pygame
import os
from sound import Sound
from color import Color
from theme import Theme

class Config: 
    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.themes = self.themes[self.idx] #current
        self.font = pygame.font.SysFont('Arial', 24)
        base_path = os.path.dirname(os.path.dirname(__file__))
        self.move_sound = Sound(os.path.join(base_path, 'assets', 'sounds', 'move.wav'))
        self.capture_sound = Sound(os.path.join(base_path, 'assets', 'sounds', 'capture.wav'))
        # self.check_sound = Sound(os.path.join('assets','sounds','check.wav')  )
        # self.checkmate_sound = Sound(os.path.join('assets','sounds','checkmate.wav')  )
        # self.stalemate_sound = Sound(os.path.join('assets','sounds','stalemate.wav')  )
       
    def change_theme(self):
          # FIX: Operate on self.all_themes list
        num_themes = len(self.themes)
        self.idx = (self.idx + 1) % num_themes # Simple modulo arithmetic for cycling
        
        # FIX: Update the current theme from the all_themes list
        self.current_theme = self.themes[self.idx]

    def _add_themes(self):
        green_theme = Theme(
            light_bg = (240,217,181), dark_bg = (181,136,99),
            light_trace = (246,246,105), dark_trace = (186,202,68),
            # highlight = (246,246,105,100),
            light_moves = (106, 246, 105), dark_moves = (68, 186, 68 ))
        
        brown_theme = Theme(light_bg=(222,184,135), dark_bg=(139,69,19),
            light_trace = (255, 228, 181), dark_trace = (205, 133, 63),
            # highlight = (255, 228, 181,100),
            light_moves = (255, 160, 122), dark_moves = (205, 112, 84))
        
        blue_theme = Theme( light_bg=(173,216,230), dark_bg=(25,25,112),
            light_trace = (135,206,250), dark_trace = (0,0,139), light_moves=(135,206,250), dark_moves=(0,0,139),)
        
        gray_theme = Theme(light_bg=(211,211,211), dark_bg=(169,169,169),
            light_trace = (192,192,192), dark_trace = (105,105,105),
            # highlight = (192,192,192,100),
            light_moves = (255, 160, 122), dark_moves = (205, 112, 84))
        
        self.themes = [green_theme, brown_theme, blue_theme, gray_theme]