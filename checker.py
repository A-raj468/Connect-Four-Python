from generator import Generator
from solver import Solver

ALL = -1


class Checker:
    def __init__(self) -> None:
        self.generator = Generator()

    def check(self, file_path: str, start: int = 0, num_test: int = -1):
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = lines[start : start + num_test] if num_test >= 0 else lines

            correctWinCount = 0
            correctScoreCount = 0
            total_test_cases = 0

            total_nodes_evaluated = 0
            total_time_taken = 0
            for line in lines:
                moves, score = line.strip().split(" ")
                score = int(score)
                board, curr_player = self.generator.generate_board(moves=moves)
                solver = Solver(board)
                winner = curr_player if score > 0 else 3 - curr_player
                winner = 0 if score == 0 else winner
                # self.generator.print_board()
                my_winner, my_score, my_move = solver.solve(curr_player)
                winner_correct = winner == my_winner
                score_correct = score == my_score
                # print(moves, curr_player)
                # print(winner_correct, winner, my_winner, score_correct, score, my_score)
                if winner_correct:
                    correctWinCount += 1

                if score_correct:
                    correctScoreCount += 1

                total_test_cases += 1
                nodes, time_in_us = solver.performance()

                total_nodes_evaluated += nodes
                total_time_taken += time_in_us

            print(
                f"Total Test Cases: {total_test_cases}",
                f"Total Correct Win: {correctWinCount}, {correctWinCount/total_test_cases*100}%",
                f"Total Correct Score: {correctScoreCount}, {correctScoreCount/total_test_cases*100}%",
                f"Average Number of Nodes Evaluated: {total_nodes_evaluated/total_test_cases}",
                f"Average Time Taken: {total_time_taken/total_test_cases}",
                sep="\n",
            )
