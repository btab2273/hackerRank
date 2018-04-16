import numpy as np

# N determines the rows of the array, M determines the columns
N, M = map(int, input().split())

# Fix the output formatting to match the expected output
np.set_printoptions(sign=' ')

print(np.eye(N, M))
