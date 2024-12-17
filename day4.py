import numpy as np
with open('data\\day4_input.txt', 'r') as f:
    data = f.read().splitlines()

#  horizontal, vertical, diagonal, written backwards ->
#   horizontal (forward), horizontal (backward), vertical (up), vertical (down), 
#   diagonal (UL -> LR), diagonal (LR -> UL), diagonal (UR -> LL), diagonal (LL -> UR)

# Example Data
# data = [['a', 'b', 'c', 'd'], 
#         ['e', 'f', 'g', 'h'], 
#         ['i', 'j', 'k', 'l'], 
#         ['m', 'n', 'o', 'p']]


# Create strings for cardinal directions
data_forward = ([''.join(x) for x in data])
data_backward = ([''.join(x[::-1]) for x in data])

data_down = [''.join(x) for x in zip(*data)]
data_up = [''.join(x) for x in zip(*data[::-1])]


# Create indirection indices for diagonal directions

# idx = [[[0,0]], 
#        [[0,1], [1,0]], 
#        [[0,2], [1,1], [2,0]], 
#        [[0,3], [1,2], [2,1], [3,0]], 
#        [[1, 3], [2, 2], [3, 1]], 
#        [[2, 3], [3, 2]], 
#        [[3, 3]]]

data_diag_UR_idx = []
for col in range(len(data)):
    d = [[row, col-row] for row in range(col+1)]
    data_diag_UR_idx.append(d)

for row in range(1, len(data)):
    d = [[row+col, len(data)-col-1] for col in range(len(data)-row)]
    data_diag_UR_idx.append(d)

# idx = [[[0,3]], 
#        [[0,2], [1,3]], 
#        [[0,1], [1,2], [2,3]], 
#        [[0,0], [1,1], [2,2], [3,3]], 
#        [[1, 0], [2, 1], [3, 2]], 
#        [[2, 0], [3, 1]], 
#        [[3, 0]]]

data_diag_UL_idx = []
for col in range(len(data), 0, -1):
    d = [[row, col+row-1] for row in range(len(data)-col+1)]
    data_diag_UL_idx.append(d)

for row in range(1, len(data)):
    d = [[row+col, col] for col in range(len(data)-row)]
    data_diag_UL_idx.append(d)

# Create strings for diagonal directions
data_diag_UL = []
data_diag_DR = []
for indices in data_diag_UL_idx:
    d_forward = [data[row][col] for row,col in indices]
    data_diag_UL.append(''.join(d_forward))
    d_backward = [data[row][col] for row,col in indices[::-1]]
    data_diag_DR.append(''.join(d_backward))

data_diag_UR = []
data_diag_DL = []
for indices in data_diag_UR_idx:
    d_forward = [data[row][col] for row,col in indices]
    data_diag_UR.append(''.join(d_forward))
    d_backward = [data[row][col] for row,col in indices[::-1]]
    data_diag_DL.append(''.join(d_backward))

# Find all matches
all_data = data_forward + data_backward + data_down + data_up + data_diag_UL + data_diag_DR + data_diag_UR + data_diag_DL
import re
search_string = r'XMAS'
print(sum([len(re.findall(search_string, x)) for x in all_data]))


# Part 2
# Find all matches of the form:
#   M.S
#   .A.
#   M.S
# 
# The MAS will always be diagonal, and the M and A can be in any order

a_indices = []
for r_idx in range(1, len(data)-1):
    for c_idx in range(1, len(data)-1):
        if data[r_idx][c_idx] == 'A':
            a_indices.append((r_idx, c_idx))
            
S = 0
for a in a_indices:
    r_idx, c_idx = a
    UL_diag_MAS = (data[r_idx-1][c_idx-1] == 'M' and data[r_idx+1][c_idx+1] == 'S') or \
                  (data[r_idx-1][c_idx-1] == 'S' and data[r_idx+1][c_idx+1] == 'M')

    UR_diag_MAS = (data[r_idx-1][c_idx+1] == 'M' and data[r_idx+1][c_idx-1] == 'S') or \
                  (data[r_idx-1][c_idx+1] == 'S' and data[r_idx+1][c_idx-1] == 'M')
    
    if UL_diag_MAS and UR_diag_MAS:
        S+=1
print(S)