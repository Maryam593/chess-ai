class Square: 
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def get_pos(self):
        return self.row, self.col
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color   
    
    def has_piece(self):
        return self.piece is not None
    
    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color
    
    def isempty_or_rival(self, color):
        return not self.has_piece() or self.piece.color != color    
    