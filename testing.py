from checker import Checker

checker = Checker()
file_path = "test_cases/Test_L3_R1"

START_TEST = 0
NUM_TEST = -1
checker.check(file_path=file_path, start=START_TEST, num_test=NUM_TEST)
