import numpy as np
import sys
universe = sys.stdin.readlines()

universe = np.array([[1 if char == '#' else 0 for char in row.strip()] for row in universe])

for i in range(universe.shape[0] - 1, -1, -1):
    if np.all(universe[i] == 0):
        universe = np.insert(universe, i, np.zeros(universe.shape[1]), axis=0)
for i in range(universe.shape[1] - 1, -1, -1):
    if np.all(universe[:, i] == 0):
        universe = np.insert(universe, i, np.zeros(universe.shape[0]), axis=1)

galaxies = []
for y, row in enumerate(universe):
    for x, char in enumerate(row):
        if char == 1:
            galaxies.append((x, y))

distance = 0
for x0, y0 in galaxies:
    for x1, y1 in galaxies:
        distance += abs(x0 - x1) + abs(y0 - y1)

print(distance//2)