from const import *
from square import Square
from piece import *
from move import Move

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
        moves = []

        if piece.name == "Pawn":
            direction = -1 if piece.color == 'white' else 1

            # Forward move (only if empty)
            if 0 <= row + direction < ROWs:
                if not self.squares[row + direction][col].has_piece():
                    moves.append((row + direction, col))

                    # Initial 2-square move
                    start_row = 6 if piece.color == 'white' else 1
                    if row == start_row and not self.squares[row + 2*direction][col].has_piece():
                        moves.append((row + 2*direction, col))

            # Diagonal captures (only if opponent piece exists)
            for dc in [-1, 1]:
                capture_row = row + direction
                capture_col = col + dc
                if 0 <= capture_row < ROWs and 0 <= capture_col < COLs:
                    if self.squares[capture_row][capture_col].has_rival_piece(piece.color):
                        moves.append((capture_row, capture_col))

        elif piece.name == "Rook":
            # Move in all 4 directions until blocked
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        # Can capture opponent piece, then stop
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r, c))
                        break
                    moves.append((r, c))
                    r, c = r + dr, c + dc
        elif piece.name == "Knight":
            knight_moves = [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)
            ]
            for r, c in knight_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    # Can't capture own pieces
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r, c))
        elif piece.name == "Bishop":
            # Move in all 4 diagonal directions until blocked
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r, c))
                        break
                    moves.append((r, c))
                    r, c = r + dr, c + dc        
        elif piece.name == "Queen":
            # Queen = Rook + Bishop (all 8 directions)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r, c))
                        break
                    moves.append((r, c))
                    r, c = r + dr, c + dc
        elif piece.name == "King":
            king_moves = [
                (row + 1, col), (row - 1, col),
                (row, col + 1), (row, col - 1),
                (row + 1, col + 1), (row + 1, col - 1),
                (row - 1, col + 1), (row - 1, col - 1)
            ]
            for r, c in king_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    # Can't capture own pieces
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r, c))
        else:
            print(f"Move calculation for {piece.name} not implemented.")
        return moves    
    
    def validate_move(self, piece, move):
        possible_moves = self.calculate_moves(piece, move.start_pos[0], move.start_pos[1])
        return move.end_pos in possible_moves

    def move(self, piece, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Remove piece from start position
        self.squares[start_row][start_col].piece = None

        # Place piece at end position
        self.squares[end_row][end_col].piece = piece

        # Mark piece as moved
        piece.moved = True

# Debugging
if __name__ == "__main__":
    b = Board()
    b.print_board()
