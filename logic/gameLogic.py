class Game():
    def __init__(self) -> None:
        self.board = [[None for _ in range(20)] for _ in range(20)]
        self.currentPLayer = 1
        