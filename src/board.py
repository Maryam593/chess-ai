from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self, game):
        self.game = game
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
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLs):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))

    def print_board(self):
        for row in self.squares:
            print([str(square.piece.name if square.piece else " ") for square in row])

    def calculate_moves(self, piece, row, col):
        moves = []

        if piece.name == "Pawn":
            direction = -1 if piece.color == 'white' else 1

            # forward
            if 0 <= row + direction < ROWs:
                if not self.squares[row + direction][col].has_piece():
                    moves.append((row + direction, col))

                    start_row = 6 if piece.color == 'white' else 1
                    if row == start_row and not self.squares[row + 2 * direction][col].has_piece():
                        moves.append((row + 2 * direction, col))

            # captures
            for dc in [-1, 1]:
                r = row + direction
                c = col + dc
                if 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_rival_piece(piece.color):
                        moves.append((r, c))

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
                    r += dr
                    c += dc

        elif piece.name == "Knight":
            knight_moves = [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)
            ]
            for r, c in knight_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r,c))

        elif piece.name == "Bishop":
            directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r,c))
                        break
                    moves.append((r,c))
                    r += dr
                    c += dc

        elif piece.name == "Queen":
            directions = [
                (1,0),(-1,0),(0,1),(0,-1),
                (1,1),(1,-1),(-1,1),(-1,-1)
            ]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < ROWs and 0 <= c < COLs:
                    if self.squares[r][c].has_piece():
                        if self.squares[r][c].has_rival_piece(piece.color):
                            moves.append((r,c))
                        break
                    moves.append((r,c))
                    r += dr
                    c += dc

        elif piece.name == "King":
            king_moves = [
                (row + 1, col), (row - 1, col),
                (row, col + 1), (row, col - 1),
                (row + 1, col + 1), (row + 1, col - 1),
                (row - 1, col + 1), (row - 1, col - 1)
            ]
            for r, c in king_moves:
                if 0 <= r < ROWs and 0 <= c < COLs:
                    if not self.squares[r][c].has_team_piece(piece.color):
                        moves.append((r,c))

        return moves

    def validate_move(self, piece, move):
        moves = self.calculate_moves(piece, move.start_pos[0], move.start_pos[1])
        return move.end_pos in moves

    def move(self, piece, start_pos, end_pos):
        sr, sc = start_pos
        er, ec = end_pos

        # remove from start
        self.squares[sr][sc].piece = None

        # place at end
        self.squares[er][ec].piece = piece
        piece.moved = True

        # check promotion
        if piece.name == "Pawn":
            self.check_pawn_promotion(piece, er, ec)

        self.last_move = Move(piece, start_pos, end_pos)

        # game over check
        if self.game.gameover.evaluate():
            print(f"Game Over! Winner: {self.game.gameover.winner}")
            self.game.stop_input = True

    def check_pawn_promotion(self, piece, row, col):
        if (piece.color == 'white' and row == 0) or (piece.color == 'black' and row == 7):
            self.squares[row][col].piece = Queen(piece.color)
            print(f"Pawn promoted to Queen at {(row, col)}")
