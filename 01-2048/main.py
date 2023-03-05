from random import randrange, choice

# CONSTANTS
SIZE = 4
BACKGROUND_COLOR = "#bbada0"
BLANK_COLOR = "#CCC0B4"
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
        self.score = 0
        self.board = [[Tile for _ in range(size)] for _ in range(size)]
    
    def blank_tiles(self) -> list[tuple[int, int]]:
        blanks = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    blanks.append((row, col))
        return blanks

    def spawn_tile(self, blanks: list[tuple[int, int]]) -> None:
        idx = choice(blanks)
        self.board[idx[0]][idx[1]] = Tile(number=(2 if randrange(10) else 4), row=idx[0], col=idx[1])

    def is_game_over(self, blanks, quit) -> bool:
        if quit:
            return True
        if blanks:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if i > 0 and self.board[i][j] == self.board[i - 1][j]:
                    return False
                if j > 0 and self.board[i][j] == self.board[i][j - 1]:
                    return False
        return True
    
    def swipe(self, direction):
        match command:
            case "D":
                for row in range(SIZE):
                    for col in range(SIZE):
                        if col > 0: 
                            self.board[row][col - 1], self.board[row][col] = self.board[row][col - 1] + self.board[row][col]
            case "W":
                pass

class Tile:
    def __init__(self, number, row, col):
        self.number = number
        self.row, self.col = row, col
        
        if number == 0:
            self.color = BLANK_COLOR
        elif number <= 2048:
            self.color = TILE_COLORS[number]
        else:
            self.color = SUPER_COLOR
            
    def __bool__(self):
        return not self.number
    
    def __add__(self, other):
        if self.number != other.number:
            return self, other
        return Tile(self.number * 2, self.row, self.col), Tile(0, other.row, other.col)

def main():
    while True:
        board = Board()
        quit = False
        while True:
            blanks = Board.blank_tiles()
            if Board.is_game_over(blanks, quit):
                break
            Board.spawn_tiles(blanks)
            while True:
                command = input("input... ").upper().strip()
                if command in ("Q", "W", "A", "S", "D"):
                    break
            if command == "Q":
                quit = True
            else:
                board.swipe(command)
                    
                    
                    
        

print(Game.help())