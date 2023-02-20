from random import randrange

class Board:
    size = 4
    def __init__(self) -> None:
        self.board = [ [ 0  for _ in range(Board.size) ] \
                     for _ in range(Board.size) ]
    
    def get_blank(self) -> list[tuple[int, int]]:
        blanks = []
        for i in self.board:
            for j in i:
                if j == 0:
                    blanks.append((i, j))
        return blanks
    
    def spawn_tile(self) -> None:
        num = 2 if randrange(10) != 0 else 4
        idx = self.get_blank()
        self.board[idx[0]][idx[1]] = num
        
    def game_over(self) -> bool:
        for i in range(Board.size):
            prevr = 0
            prevc = 0
            for j in range(Board.size):
                if self.board[i][j] == prevc or self.board[j][i] == prevr or self.board[i][j] == 0:
                    return True
                prevc, prevr = self.board[i][j], self.board[j][i]
        return False
    


def main():
    style = {
        "background" : "#bbada0",
        "empty" : "#CCC0B4",
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
        2048 : "#edc22e",
        "super" : "#3c3a33"
    }
    
    # main function
    while True:
        score, board, direction = init_game()
        while True:
            board.spawn_tile()
            display_game(board)
            if board.game_over():
                break
            while not board.valid_direction():
                if restart(direction):
                    break
                direction = get_direction()
            else:
                board.swipe(direction)
        alert_death(score)
        restart_game()            

if __name__ == "__main__":
    main()