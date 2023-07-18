ROWS = 6
COLS = 7

EMPTY = 0
P1 = 1
P2 = 2


class Generator:
    def __init__(self):
        self.moves = ""
        self.curr_player = P1
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]

    def generate_board(self, moves: str):
        board = [[EMPTY] * COLS for _ in range(ROWS)]

        curr_player = P1
        for move in moves:
            col = int(move) - 1
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] == EMPTY:
                    board[row][col] = curr_player
                    break

            curr_player = P2 if curr_player == P1 else P1

        self.moves = moves
        self.curr_player = curr_player
        self.board = [[j for j in i] for i in board]
        return self.board, self.curr_player

    def print_board(self):
        for i in self.board:
            for j in i:
                if j == EMPTY:
                    print("_ ", end="")
                elif j == P1:
                    print("* ", end="")
                elif j == P2:
                    print("o ", end="")

            print()
