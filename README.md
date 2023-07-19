# Connect-4 Python Solver

In this project, I created a connect-4 solver in python.

## Performance Comparision

_N/A represent could not successfully complete in given time_

### V1: Negamax(depth 6)

I used the **Negamax** variant of the **Minimax** algorithm.

| Test Set (1000 test cases each) | Test Set Level | Correct Winner | Correct Score | Avg. No. of Nodes | Avg. Time Taken   |
| ------------------------------- | -------------- | -------------- | ------------- | ----------------- | ----------------- |
| **Test_L3_R1**                  | End-Easy       | 676            | 643           | 5001.265          | 81294.95692253112 |
| **Test_L2_R1**                  | Middle-Easy    | N/A            | N/A           | N/A               | N/A               |
| **Test_L2_R2**                  | Middle-Medium  | N/A            | N/A           | N/A               | N/A               |
| **Test_L1_R1**                  | Begin-Easy     | N/A            | N/A           | N/A               | N/A               |
| **Test_L1_R2**                  | Begin-Medium   | N/A            | N/A           | N/A               | N/A               |
| **Test_L1_R3**                  | Begin-Hard     | N/A            | N/A           | N/A               | N/A               |

### V2: Alpha-Beta Pruning

I optimized it using the **Aplha-Beta Pruning** technique along with better move ordering to reduce the number of nodes searched, thus improving the performance.
