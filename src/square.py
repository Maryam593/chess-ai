class Square: 
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def get_pos(self):
        return self.row, self.col
    
    def has_piece(self):
        return self.piece is not None