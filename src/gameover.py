# gameover.py

class GameOver:
    def __init__(self, game):
        """
        game: reference to your Game instance (so we can access board, sounds, UI flags).
        """
        self.game = game
        self.is_over = False
        self.winner = None
        self.reason = None  # optional: "king_captured", "checkmate", "resign", etc.

    def reset(self):
        self.is_over = False
        self.winner = None
        self.reason = None

    def check_kings_alive(self):
        """
        Simple scan: return (white_alive, black_alive)
        """
        white_alive = False
        black_alive = False

        for row in range(self.game.ROWS):
            for col in range(self.game.COLS):
                sq = self.game.board.squares[row][col]
                if sq.has_piece():
                    p = sq.piece
                    if p.name == 'king':
                        if p.color == 'white':
                            white_alive = True
                        elif p.color == 'black':
                            black_alive = True

        return white_alive, black_alive

    def evaluate(self):
        """
        Call this after every move. Determines if game should stop.
        Returns True if game just became over (so caller can react).
        """
        if self.is_over:
            return True

        white_alive, black_alive = self.check_kings_alive()

        if not white_alive and not black_alive:
            # extremely unlikely but handle both gone
            self.is_over = True
            self.winner = None
            self.reason = 'both_kings_missing'
            return True

        if not white_alive:
            self.is_over = True
            self.winner = 'black'
            self.reason = 'king_captured'
            return True

        if not black_alive:
            self.is_over = True
            self.winner = 'white'
            self.reason = 'king_captured'
            return True

        # Placeholder for future: implement check/checkmate here
        # if self._is_checkmate('white'): ...
        return False

    # OPTIONAL: stub for checkmate detection later
    def _is_checkmate(self, color):
        """
        Complex: must check if 'color' is in check and has NO legal moves.
        Return True/False. Keep as placeholder for now.
        """
        return False
