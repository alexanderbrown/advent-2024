from copy import deepcopy
from collections import defaultdict
with open('data\\day6_input.txt', 'r') as f:
    data = f.read().splitlines()

# data = \
# """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".splitlines()

guard_symbols = ['^',  '>', 'v', '<']

def find_guard(input):
    for idx, line in enumerate(input):
        for direction, symbol in enumerate(guard_symbols):
            if symbol in line:
                x = line.index(symbol)
                y = idx
                return x, y, direction
    raise ValueError("No guard found")

def move_guard(input, already_visited=None):
    x,y,direction = find_guard(input)
    x1,y1 = x,y
    if direction == 0:
        y1 -= 1
    elif direction == 1:
        x1 += 1
    elif direction == 2:
        y1 += 1
    elif direction == 3:
        x1 -= 1

    if already_visited is not None:
        if direction in already_visited[y][x]:
            return None # distinguishable from False, but still not truthy
        
        already_visited[y][x].append(direction)
    # If we are at the edge of the map, finish
    if y1 < 0 or y1 >= len(input) or x1 < 0 or x1 >= len(input[0]):
        input[y][x] = 'X'
        return False
    # Turn right if there is a wall in front
    if input[y1][x1] == '#':
        input[y][x] = guard_symbols[(direction+1)%4]
    else:
        input[y][x] = 'X'
        input[y1][x1] = guard_symbols[direction]
    return True

already_visited = defaultdict(lambda: defaultdict(list))
input = deepcopy(data)
input = [list(x) for x in input]
while True:
    should_continue = move_guard(input, already_visited)
    if not should_continue:
        break    
result_part1 = deepcopy(input)

# for line in result_part1:
#     print(''.join(line))

print(f'{sum([x.count('X') for x in input])} steps to exit')

# Part 2

previously_visited = [[y, x] for y in already_visited for x in already_visited[y]]
# print(previously_visited)

identified_loops = 0
for idx, obstacle_location in enumerate(previously_visited[1:]):
    print(f'Checking obstacle {idx+1} of {len(previously_visited)}, {identified_loops} loops found so far')
    already_visited = defaultdict(lambda: defaultdict(list))
    input = deepcopy(data)
    input = [list(x) for x in input]
    input[obstacle_location[0]][obstacle_location[1]] = '#'
    while True:
        should_continue = move_guard(input, already_visited)
        if not should_continue:
            if should_continue is None:
                identified_loops += 1
            break

print(f'{identified_loops} postitions found that cause a loop')