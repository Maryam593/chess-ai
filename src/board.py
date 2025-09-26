from turtle import color
from const import *
from square import Square
from piece import *
class Board:
    def __init__(self):
        # pass
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLs)]
        self.create_board() 
        self.add_pieces('white')
        self.add_pieces('black')

    def create_board(self):
        for row in range(ROWs):
            for col in range(COLs):
                self.squares[row][col] = Square(row,col)
   
    def add_pieces(self, color):
    # Adding Pawns
     row_pawn, row_other = (6,7) if color == 'white' else (1,0)
     for col in range(COLs):
        # pawns
        self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

    # Adding knights
     self.squares[row_other][1] = Square(row_other, 1, Knight(color))
     self.squares[row_other][6] = Square(row_other, 6, Knight(color))

    # Adding bishops
     self.squares[row_other][2] = Square(row_other, 2, Bishop(color)) 
     self.squares[row_other][5] = Square(row_other, 5, Bishop(color)) 

    # Adding rooks
     self.squares[row_other][0] = Square(row_other, 0, Rook(color))    
     self.squares[row_other][7] = Square(row_other, 7, Rook(color))

    # Adding queen
     self.squares[row_other][3] = Square(row_other, 3, Queen(color))   

    # Adding king
     self.squares[row_other][4] = Square(row_other, 4, King(color))    

    # Debugging: print board pieces row by row
     self.print_board()


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
        print(self.squares)

b = Board()
b.create_board()