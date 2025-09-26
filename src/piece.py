import os

class Piece:
    def __init__(self, name, color, value, texture="", texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign
        self.texture = texture
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False

    def set_texture(self, size=80):
        # Normalize: file names ko lowercase karte hain for safety
        filename = f"{self.color}_{self.name}".lower() + ".png"
        self.texture = os.path.join(
            os.path.dirname(__file__),
            f"../assets/images/imgs-{size}px/{filename}"
        )

    def add_moves(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("Pawn", color, 1)
        self.set_texture()


class Rook(Piece):
    def __init__(self, color):
        super().__init__("Rook", color, 5)
        self.set_texture()


class Knight(Piece):
    def __init__(self, color):
        super().__init__("Knight", color, 3)
        self.set_texture()


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("Bishop", color, 3)
        self.set_texture()


class Queen(Piece):
    def __init__(self, color):
        super().__init__("Queen", color, 9)
        self.set_texture()


class King(Piece):
    def __init__(self, color):
        super().__init__("King", color, 0)
        self.set_texture()


# Testing the Piece classes
if __name__ == "__main__":
    white_pawn = Pawn("white")
    black_king = King("black")

    print(f"{white_pawn.name} - Color: {white_pawn.color}, Value: {white_pawn.value}, Texture: {white_pawn.texture}")
    print(f"{black_king.name} - Color: {black_king.color}, Value: {black_king.value}, Texture: {black_king.texture}")
