class Board:
    # def __init__(self, rows, cols):
    #     self.rows = rows
    #     self.cols = cols
    #     self.board = [[None for _ in range(cols)] for _ in range(rows)]

    # def get_square(self, row, col):
    #     if 0 <= row < self.rows and 0 <= col < self.cols:
    #         return self.board[row][col]
    #     return None

    # def set_square(self, row, col, piece):
    #     if 0 <= row < self.rows and 0 <= col < self.cols:
    #         self.board[row][col] = piece

    # def print_board(self):
    #     for row in self.board:
    #         print(" | ".join([str(piece) if piece else '.' for piece in row]))
    #         print("-" * (self.cols * 4 - 1))

    def __init__(self):
        # pass
        self.squares = []
        self.create_board() 
        
    def create_board(self):
        pass
    def add_pieces(self,color):
        pass
    def move_piece(self):
        pass
    def get_piece(self):
        pass
    def remove_piece(self):
        pass
    def is_in_check(self):
        pass
    def is_checkmate(self):
        pass
    def is_stalemate(self):
        pass
    def get_all_moves(self):
        pass
    def evaluate_board(self):
        pass
    def print_board(self):
        pass                    