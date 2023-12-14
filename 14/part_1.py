import sys
import numpy as np

platform = np.array([list(line) for line in sys.stdin.read().splitlines()])
height_of_platform = platform.shape[0]

sol = 0
for column_index in range(platform.shape[1]):
    column = platform[:, column_index]
    num_empties = num_rocks = 0
    new_column = []
    points = 0

    for i, element in enumerate(column):
        if element == '.':
            num_empties += 1
        elif element == 'O':
            num_rocks += 1
        elif element == '#':
            for _ in range(num_rocks):
                new_column.append('0')
                points += (height_of_platform - len(new_column) + 1)
            for _ in range(num_empties):
                new_column.append('.')
            num_empties = num_rocks = 0
            new_column.append(element)
        else:
            raise Exception(f'Invalid element {element} at {i, column_index}')
    
    for _ in range(num_rocks):
        new_column.append('0')
        points += (height_of_platform - len(new_column) + 1)
    for _ in range(num_empties):
        new_column.append('.')

    sol += points
print(sol)
    