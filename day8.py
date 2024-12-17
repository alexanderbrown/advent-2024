"""Day 8."""
import re
from os import path

with open(path.join('data', 'input_day8.txt'), 'r', encoding='utf-8') as f:
    FULL_DATA = f.read()

EXAMPLE_DATA = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()

SIMPLE_PART_2_EXAMPLE = """
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
""".strip()

def check_in_bounds(antinode: tuple[int, int], width: int, height:int):
    """Checks a proposed location is within the grid."""
    return antinode[0] >=0 and antinode[0] < width and antinode[1] >=0 and antinode[1] < height

def get_tower_locations(tower_type: str, data:str, width:int, height:int):
    """Get the x and y location of towers."""
    indices = [m.start() for m in re.finditer(tower_type, data.replace('\n', ''))]
    x = [i // width for i in indices]
    y = [i % height for i in indices]
    return x,y

def get_proposed_locations(t1_x, t2_x, t1_y, t2_y) -> tuple[tuple[int, int], tuple[int, int]]:
    """Get proposed locations, either side of a tower."""
    delta_x = t2_x - t1_x
    delta_y = t2_y - t1_y

    antinode_1 = (t1_x - delta_x, t1_y - delta_y)
    antinode_2 = (t2_x + delta_x, t2_y + delta_y)

    return antinode_1, antinode_2

#pylint: disable=too-many-arguments
def get_part2_proposed_locations(t1_x, t2_x, t1_y, t2_y, 
                                 width, height) -> list[tuple[int, int]]:
    """Similar to the above, but allow any number of whole grid locations in bounds.
    Checks locations are in bounds too"""
    delta_x = t2_x - t1_x
    delta_y = t2_y - t1_y

    locs = []
    # One side of one antenna
    proposed_loc = [t1_x, t1_y]
    while True:
        proposed_loc[0]-= delta_x
        proposed_loc[1]-= delta_y
        if proposed_loc[0] >= 0 and proposed_loc[1] >= 0 and \
            proposed_loc[0] < width and proposed_loc[1] < height:
            locs.append([proposed_loc[0], proposed_loc[1]])
        else:
            break

    # Other side of other antenna
    proposed_loc = [t2_x, t2_y]
    while True:
        proposed_loc[0]+= delta_x
        proposed_loc[1]+= delta_y
        if proposed_loc[0] >= 0 and proposed_loc[1] >= 0 and \
            proposed_loc[0] < width and proposed_loc[1] < height:
            locs.append([proposed_loc[0], proposed_loc[1]])
        else:
            break
    return locs

def part_1(data):
    """Main function for part 1"""
    width = len(data.splitlines())
    height = len(data.splitlines()[0])
    tower_types = set(data) - set(('\n', '.'))
    antinode_locations = []
    for tower_type in tower_types:
        x,y = get_tower_locations(tower_type, data, width=width, height=height)
        for idx, (t1_x, t1_y) in enumerate(zip(x,y)):
            for t2_x, t2_y in zip(x[idx:],y[idx:]):
                if t1_x == t2_x and t1_y == t2_y:
                    continue

                antinodes = get_proposed_locations(t1_x=t1_x, t2_x=t2_x, t1_y=t1_y, t2_y=t2_y)
                for antinode in antinodes:
                    if check_in_bounds(antinode, width, height) and \
                                    antinode not in antinode_locations:
                        antinode_locations.append(antinode)
    return len(antinode_locations)

def part_2(data):
    """Main function for part 2."""
    width = len(data.splitlines())
    height = len(data.splitlines()[0])
    tower_types = set(data) - set(('\n', '.'))
    antinode_locations = []
    for tower_type in tower_types:
        x,y = get_tower_locations(tower_type, data, width=width, height=height)
        for idx, (t1_x, t1_y) in enumerate(zip(x,y)):
            for t2_x, t2_y in zip(x[idx:],y[idx:]):
                if t1_x == t2_x and t1_y == t2_y:
                    continue

                antinodes = get_part2_proposed_locations(
                    t1_x=t1_x, t2_x=t2_x, t1_y=t1_y, t2_y=t2_y,
                    width=width, height=height)

                for antinode in antinodes:
                    if antinode not in antinode_locations:
                        antinode_locations.append(antinode)
        # Add towers themselves:
        for xi, yi in zip(x, y):
            if [xi, yi] not in antinode_locations:
                antinode_locations.append([xi, yi])
    return len(antinode_locations)

if __name__=='__main__':
    print(f'Part 1, Example data: {part_1(EXAMPLE_DATA)}')
    print(f'Part 1, Full data: {part_1(FULL_DATA)}')
    print(f'Part 2, Simple Example data: {part_2(SIMPLE_PART_2_EXAMPLE.replace('#', '.'))}')
    print(f'Part 2, Example data: {part_2(EXAMPLE_DATA)}')
    print(f'Part 2, Full data: {part_2(FULL_DATA)}')
