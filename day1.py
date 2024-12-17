import numpy as np
import pandas as pd

data = pd.read_csv('data\\day1_input.txt', header=None, sep='   ')

col1_sorted = data[0].sort_values().to_numpy()
col2_sorted = data[1].sort_values().to_numpy()

distances = np.abs(col1_sorted - col2_sorted)
print(f'Part 1: {distances.sum()}')

similarity = 0
for left in col1_sorted:
    matches = np.sum(col2_sorted == left)
    similarity += left*matches

print(f'Part 2: {similarity}')