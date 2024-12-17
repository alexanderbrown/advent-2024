"""Day 7."""
from os import path
from typing import Callable, LiteralString, Sequence

with open(path.join('data', 'input_day7.txt'), 'r', encoding='utf-8') as f:
    full_data = f.readlines()

example_data="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

def process_input(raw_data: Sequence[str| LiteralString]) -> tuple[tuple[int, tuple[int]], ...]:
    """Process raw input"""
    data_processed = []
    for line in raw_data:
        k, remainder = line.split(':')
        v = tuple((int(n) for n in remainder.split()))
        data_processed.append(tuple([int(k), v]))
    return tuple(data_processed)

def attempt(col: int, remaining: Sequence[int], 
            allowed_operations: tuple[Callable[[int, int], int], ...] ):
    """Find all possible results of the allowed operations, with depth-first search."""

    next_number = remaining[0]
    results = []
    for operation in allowed_operations:
        new_col = operation(col, next_number)
        if len(remaining) > 1:
            results.extend(attempt(new_col, remaining[1:], allowed_operations))
        else:
            results.append(new_col)
    return results

def try_solve(target: int, inputs: Sequence[int], allowed_operations):
    """Set up and run DFS"""
    results = attempt(inputs[0], inputs[1:], allowed_operations)
    return target in results

def main(input_data, allowed_operations):
    """Main function"""
    processed_data = process_input(input_data)
    total = 0
    for target, inputs in processed_data:
        if try_solve(target, inputs, allowed_operations):
            total +=target
    print(total)


if __name__ == '__main__':
    ops = (
        lambda x,y: x+y,
        lambda x,y: x*y
    )
    main(example_data, ops)
    main(full_data, ops)

    ops = (
        lambda x,y: x+y,
        lambda x,y: x*y, 
        lambda x,y: int(str(x)+str(y))
    )
    main(example_data, ops)
    main(full_data, ops)
