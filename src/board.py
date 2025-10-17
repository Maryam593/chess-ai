from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        # ✅ Initialize 8x8 board
        self.squares = [[None for col in range(COLs)] for row in range(ROWs)]
        self.create_board()
        self.add_pieces('white')
        self.add_pieces('black')
        self.last_move = None 

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

            # Forward move
            if 0 <= row + direction < ROWs:
                if not self.squares[row + direction][col].has_piece():
                    moves.append((row + direction, col))

                    # 2-step initial move
                    start_row = 6 if piece.color == 'white' else 1
                    if row == start_row and not self.squares[row + 2*direction][col].has_piece():
                        moves.append((row + 2*direction, col))

            # Diagonal captures
            for dc in [-1, 1]:
                capture_row = row + direction
                capture_col = col + dc
                if 0 <= capture_row < ROWs and 0 <= capture_col < COLs:
                    if self.squares[capture_row][capture_col].has_rival_piece(piece.color):
                        moves.append((capture_row, capture_col))

        elif piece.name == "Rook":
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r,c))
                        break
                    moves.append((r,c))
                    r, c = r + dr, c + dc

        elif piece.name == "Knight":
            knight_moves = [
                (row+2, col+1), (row+2, col-1),
                (row-2, col+1), (row-2, col-1),
                (row+1, col+2), (row+1, col-2),
                (row-1, col+2), (row-1, col-2)
            ]
            for r, c in knight_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r,c))

        elif piece.name == "Bishop":
            directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r,c))
                        break
                    moves.append((r,c))
                    r, c = r + dr, c + dc        

        elif piece.name == "Queen":
            directions = [
                (1,0), (-1,0), (0,1), (0,-1),
                (1,1), (1,-1), (-1,1), (-1,-1)
            ]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r,c))
                        break
                    moves.append((r,c))
                    r, c = r + dr, c + dc

        elif piece.name == "King":
            king_moves = [
                (row+1, col), (row-1, col),
                (row, col+1), (row, col-1),
                (row+1, col+1), (row+1, col-1),
                (row-1, col+1), (row-1, col-1)
            ]
            for r, c in king_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r,c))

            # Include castling options
            for castle in self.king_castling_moves(piece.color):
                moves.append(castle)

        else:
            print(f"Move calculation for {piece.name} not implemented.")
        return moves    

    def validate_move(self, piece, move):
        possible_moves = self.calculate_moves(piece, move.start_pos[0], move.start_pos[1])
        return move.end_pos in possible_moves

    def move(self, piece, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # ✅ Handle castling BEFORE moving king
        if piece.name == "King" and not piece.moved:
            row = start_row

            # Kingside castling
            if end_col == 6 and self.squares[row][5].piece is None and self.squares[row][6].piece is None:
                rook = self.squares[row][7].piece
                if rook and rook.name == "Rook" and not rook.moved:
                    # Move king
                    self.squares[start_row][start_col].piece = None
                    self.squares[end_row][end_col].piece = piece
                    piece.moved = True
                    # Move rook
                    self.squares[row][5].piece = rook
                    self.squares[row][7].piece = None
                    rook.moved = True
                    self.last_move = Move(piece, start_pos, end_pos)
                    return

            # Queenside castling
            if end_col == 2 and all(self.squares[row][i].piece is None for i in [1,2,3]):
                rook = self.squares[row][0].piece
                if rook and rook.name == "Rook" and not rook.moved:
                    self.squares[start_row][start_col].piece = None
                    self.squares[end_row][end_col].piece = piece
                    piece.moved = True
                    # Move rook
                    self.squares[row][3].piece = rook
                    self.squares[row][0].piece = None
                    rook.moved = True
                    self.last_move = Move(piece, start_pos, end_pos)
                    return

        # Normal move
        self.squares[start_row][start_col].piece = None
        self.squares[end_row][end_col].piece = piece
        piece.moved = True

        # Pawn promotion check
        if piece.name == "Pawn":
            self.check_pawn_promotion(piece, end_row, end_col)

        self.last_move = Move(piece, start_pos, end_pos)

    def check_pawn_promotion(self, piece, row, col):
        if (piece.color == 'white' and row == 0) or (piece.color == 'black' and row == 7):
            self.squares[row][col].piece = Queen(piece.color)
            print(f"Pawn promoted to Queen at {(row, col)}")

    def king_castling_moves(self, color):
        moves = []
        row = 7 if color == 'white' else 0
        king = self.squares[row][4].piece

        if king and not king.moved:
            # Kingside
            if (self.squares[row][5].piece is None and self.squares[row][6].piece is None):
                rook = self.squares[row][7].piece
                if rook and rook.name == "Rook" and not rook.moved:
                    moves.append((row, 6))

            # Queenside
            if (self.squares[row][1].piece is None and
                self.squares[row][2].piece is None and
                self.squares[row][3].piece is None):
                rook = self.squares[row][0].piece
                if rook and rook.name == "Rook" and not rook.moved:
                    moves.append((row, 2))

        return moves

# Debugging
if __name__ == "__main__":
    b = Board()
    b.print_board()
