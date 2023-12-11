import numpy as np
import sys
universe = sys.stdin.readlines()

universe = np.array([[1 if char == '#' else 0 for char in row.strip()] for row in universe])

empty_rows = np.where(np.all(universe == 0, axis=1))[0]
empty_cols = np.where(np.all(universe == 0, axis=0))[0]
rows = np.zeros(len(universe))
cols = np.zeros(len(universe[0]))
for row in empty_rows:
    rows[row] = 1
for col in empty_cols:
    cols[col] = 1

galaxies = []
for y, row in enumerate(universe):
    for x, char in enumerate(row):
        if char == 1:
            galaxies.append((x, y))

expansion_factor = 1_000_000-1
total_distance = 0
for x0, y0 in galaxies:
    for x1, y1 in galaxies:
        num_empty_rows = np.sum(rows[min(y0, y1):max(y0, y1)])
        num_empty_cols = np.sum(cols[min(x0, x1):max(x0, x1)])
        distance = (num_empty_rows + num_empty_cols) * expansion_factor + abs(x0 - x1) + abs(y0 - y1)
        total_distance += distance

print(total_distance//2)
