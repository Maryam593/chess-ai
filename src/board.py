from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        # ✅ Proper 8x8 board initialize karo
        self.squares = [[None for col in range(COLs)] for row in range(ROWs)]
        self.create_board()
        self.add_pieces('white')
        self.add_pieces('black')

    def create_board(self):
        for row in range(ROWs):
            for col in range(COLs):
                if self.squares[row][col] is None:
                    self.squares[row][col] = Square(row, col)

    def add_pieces(self, color):
        # Pawns
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        for col in range(COLs):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))

    def print_board(self):
        for row in self.squares:
            print([str(square.piece.name if square.piece else " ") for square in row])
   
    def calculate_moves(self, piece, row, col):
        # Placeholder for move calculation logic
        moves = []
        if piece.name == "Pawn":
            direction = -1 if piece.color == 'white' else 1
            if 0 <= row + direction < ROWs:
                moves.append((row + direction, col))
        # Add logic for other pieces
        elif piece.name == "Rook":
            for r in range(ROWs):
                if r != row:
                    moves.append((r, col))  
            for c in range(COLs):
                if c != col:
                    moves.append((row, c))
        elif piece.name == "Knight":    
            knight_moves = [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)
            ]
            for r, c in knight_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    moves.append((r, c))
        elif piece.name == "Bishop":
            for i in range(1, ROWs):
                if 0 <= row + i < ROWs and 0 <= col + i < COLs:
                    moves.append((row + i, col + i))
                if 0 <= row + i < ROWs and 0 <= col - i < COLs:
                    moves.append((row + i, col - i))
                if 0 <= row - i < ROWs and 0 <= col + i < COLs:
                    moves.append((row - i, col + i))
                if 0 <= row - i < ROWs and 0 <= col - i < COLs:
                    moves.append((row - i, col - i))        
        elif piece.name == "Queen":
            for r in range(ROWs):
                if r != row:
                    moves.append((r, col))  
            for c in range(COLs):
                if c != col:
                    moves.append((row, c))
            for i in range(1, ROWs):
                if 0 <= row + i < ROWs and 0 <= col + i < COLs:
                    moves.append((row + i, col + i))
                if 0 <= row + i < ROWs and 0 <= col - i < COLs:
                    moves.append((row + i, col - i))
                if 0 <= row - i < ROWs and 0 <= col + i < COLs:
                    moves.append((row - i, col + i))
                if 0 <= row - i < ROWs and 0 <= col - i < COLs:
                    moves.append((row - i, col - i))
        elif piece.name == "King":
            king_moves = [
                (row + 1, col), (row - 1, col),
                (row, col + 1), (row, col - 1),
                (row + 1, col + 1), (row + 1, col - 1),
                (row - 1, col + 1), (row - 1, col - 1)
            ]
            for r, c in king_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    moves.append((r, c))
        else:
            print(f"Move calculation for {piece.name} not implemented.")
        return moves    
    
# Debugging
if __name__ == "__main__":
    b = Board()
    b.print_board()
