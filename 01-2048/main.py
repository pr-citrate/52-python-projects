from random import randrange

SIZE = 4
BACKGROUND_COLOR = "#bbada0",
BLANK_COLOR = "#CCC0B4",
TILE_COLORS = {
    2 : "#eee4da",
    4 : "#eee1c9",
    8 : "#f3b27a",
    16 : "#f69664",
    32 : "#f77c5f",
    64 : "#f75f3b",
    128 : "#edd073",
    256 : "#edcc62",
    512 : "#edc950",
    1024 : "#edc53f",
    2048 : "#edc22e"
}
SUPER_COLOR = "#3c3a33"

class Board:
    def __init__(self, size=SIZE) -> None:
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
    
    def get_blank_tiles(self) -> list[tuple[int, int]]:
        blanks = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    blanks.append((row, col))
        return blanks

    def spawn_tile(self) -> None:
        num = 2 if randrange(10) != 0 else 4
        blanks = self.get_blank_tiles()
        if not blanks:
            return
        idx = randrange(len(blanks))
        row, col = blanks[idx]
        self.board[row][col] = num

    def game_over(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                if i > 0 and self.board[i][j] == self.board[i - 1][j]:
                    return False
                if j > 0 and self.board[i][j] == self.board[i][j - 1]:
                    return False
        return True
