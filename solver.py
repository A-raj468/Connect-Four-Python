import numpy as np
import time

ROWS = 6
COLS = 7
WINNING_LENGTH = 4
colsToCheck = [0, 1, 2, 3, 4, 5, 6]

EMPTY = 0
P1 = 1
P2 = 2

# Define color escape sequences
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


class Solver:
    def __init__(self, board: list[list[int]]):
        self.time_taken = 0
        self.winner = 0
        self.score = 0
        self.move = -1
        self.board = np.array(board)
        self.total_nodes_searched = 0

    def canPlay(self, col: int):
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == EMPTY:
                return row

        return -1

    def play(self, row: int, col: int, player: int):
        if self.board[row][col] != EMPTY:
            raise Exception(YELLOW + "Cell is already full!" + RESET)
        self.board[row][col] = player

    def unplay(self, row: int, col: int):
        if self.board[row][col] == EMPTY:
            raise Exception(YELLOW + "Cell already empty!" + RESET)
        self.board[row][col] = EMPTY

    def isWinning(self, row: int, col: int, player: int):
        if self.board[row][col] != EMPTY:
            raise Exception(YELLOW + "Cell is already full!" + RESET)

        # print(f"{self.board[row][col]}")
        self.play(row, col, player)

        board = self.board

        win = False
        # Check horizontally
        if not win:
            for c in range(col - WINNING_LENGTH + 1, col + WINNING_LENGTH):
                if c < 0 or c + WINNING_LENGTH > COLS:
                    continue
                if np.all(board[row][c : c + WINNING_LENGTH] == player):
                    # print(f"Horizontal: {row}, {c}")
                    win = True

        # Check vertically
        if not win:
            for r in range(row - WINNING_LENGTH + 1, row + WINNING_LENGTH):
                if r < 0 or r + WINNING_LENGTH > ROWS:
                    continue
                if np.all(board[r : r + WINNING_LENGTH, col] == player):
                    # print(f"Vertical: {r}, {col}")
                    win = True

        # Check diagonals (top-left to bottom-right)
        if not win:
            for d in range(-WINNING_LENGTH + 1, WINNING_LENGTH):
                if (
                    row + d < 0
                    or row + d + WINNING_LENGTH > ROWS
                    or col + d < 0
                    or col + d + WINNING_LENGTH > COLS
                ):
                    continue
                if np.all(
                    np.diag(
                        board[
                            row + d : row + d + WINNING_LENGTH,
                            col + d : col + d + WINNING_LENGTH,
                        ]
                    )
                    == player
                ):
                    # print(f"Diagonal1: {row}, {col}")
                    win = True

        # Check diagonals (bottom-left to top-right)
        if not win:
            for d in range(-WINNING_LENGTH + 1, WINNING_LENGTH):
                if (
                    row + d < 0
                    or row + d + WINNING_LENGTH >= ROWS
                    or col + d - WINNING_LENGTH + 1 < 0
                    or col + d + 1 > COLS
                ):
                    continue
                # print(
                #     row + d,
                #     row + d + WINNING_LENGTH,
                #     col + d - WINNING_LENGTH + 1,
                #     col + d + 1,
                #     board[
                #         row + d : row + d + WINNING_LENGTH,
                #         col + d - WINNING_LENGTH + 1 : col + d + 1,
                #     ],
                # )
                if np.all(
                    np.diag(
                        np.fliplr(
                            board[
                                row + d : row + d + WINNING_LENGTH,
                                col + d - WINNING_LENGTH + 1 : col + d + 1,
                            ]
                        )
                    )
                    == player
                ):
                    # print(f"Diagonal2: {row}, {col}")
                    win = True

        # print(f"{self.board[row][col]}")
        self.unplay(row, col)
        # print(f"{self.board[row][col]}")
        return win

    def scoreForCol(self, col: int, player: int, depth: int):
        self.total_nodes_searched += 1
        if depth == 0 or self.numMovesBeginning() == ROWS * COLS:
            return 0

        row = self.canPlay(col)
        # print(f"Row: {row}, Col: {col}, Cell: {self.board[row][col]}")
        if row != -1:
            # print(player, row, col, self.isWinning(row, col, player))
            # self.print_board()
            if self.isWinning(row, col, player):
                return (ROWS * COLS + 1 - self.numMovesBeginning()) // 2

            # print(RED + f"Reached play! {self.board[row][col]}" + RESET)
            self.play(row, col, player)
            # print(GREEN + "Passed play!" + RESET)
            if self.numMovesBeginning() == ROWS * COLS:
                return 0
            new_player = 3 - player
            all_scores = self.scoreForAllCols(new_player, depth - 1)
            # print(all_scores)
            curr_score = -max(all_scores.values())
            self.unplay(row, col)
            # print(curr_score)
            return curr_score

        else:
            raise Exception(YELLOW + "Calculating score of unplayable column" + RESET)

    def scoreForAllCols(self, player: int, depth: int):
        scores = {}
        for col in colsToCheck:
            if self.canPlay(col) != -1:
                curr_score = self.scoreForCol(col, player, depth)
                scores[col] = curr_score
        # print(f"Depth: {depth}, Player: {player}")
        # print(scores)
        return scores

    def solve(self, player: int):
        self.time_taken = time.time() * 1000_000
        scores = self.scoreForAllCols(player, 6)
        # print(scores.items())
        col, score = max(scores.items(), key=lambda x: x[1])
        if score == 0:
            self.winner == 0
        else:
            self.winner = player if score > 0 else 3 - player

        self.score = score
        self.move = col

        self.time_taken = time.time() * 1000_000 - self.time_taken
        # print(f"Move: {self.move}")
        return self.winner, self.score, self.move

    def numMovesBeginning(self):
        return np.count_nonzero(self.board)

    def performance(self):
        return self.total_nodes_searched, self.time_taken

    def print_board(self):
        print("-" * 50)
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.board[row][col]
                if cell == 0:
                    print("_ ", end="")
                elif cell == 1:
                    print("* ", end="")
                elif cell == 2:
                    print("o ", end="")
            print()
        print("-" * 50)
