import numpy as np
import sys
data = sys.stdin.readlines()

sol = 0


data_lst = []
special_symbols = []
for i, line in enumerate(data):
    line = line.strip()

    line_lst = []
    for j, char in enumerate(line):
        if char in "0123456789":
            line_lst.append(int(char))
        elif char == ".":
            line_lst.append(-1)
        else:
            special_symbols.append((i+1, j+1))
            line_lst.append(-2)
    data_lst.append(line_lst)
data_np = np.array(data_lst)
data_np = np.pad(data_np, 1, mode='constant', constant_values=-1)

w, h = data_np.shape

# Add up all numbers
for i in range(data_np.shape[0]):
    curr_num = ""
    for j in range(data_np.shape[1]):
        if data_np[i, j] >= 0:
            curr_num += str(data_np[i, j])
        else:
            if curr_num:
                sol += int(curr_num)
                curr_num = ""

# Find numbers adjacent (including corners) to special symbols and set them to -3
contagious_nums = []
for i, j in special_symbols:
    for x, y in [
        (max(0, i-1), max(0, j-1)),
        (max(0, i-1), j),
        (max(0, i-1), min(j+1, w-1)),
        (i, max(0, j-1)),
        (i, j),
        (i, min(j+1, w-1)),
        (min(i+1, h-1), max(0, j-1)),
        (min(i+1, h-1), j),
        (min(i+1, h-1), min(j+1, w-1))
    ]:
        if data_np[x, y] >= 0:
            data_np[x, y] = -3
            contagious_nums.append((x, y))

# Propagate -3s (contagious_nums) until no numbers are adjacent to -3s on the x-axis
while True:
    new_contagious_nums = []
    for i, j in contagious_nums:
        for x, y in [(i, max(0, j-1)), (i, min(j+1, w-1))]:
            if data_np[x, y] >= 0:
                data_np[x, y] = -3
                new_contagious_nums.append((x, y))
    contagious_nums = new_contagious_nums
    if not contagious_nums:
        break

# Set all negative numbers to -1
data_np[data_np < 0] = -1

# Add up all numbers left
for i in range(data_np.shape[0]):
    curr_num = ""
    for j in range(data_np.shape[1]):
        if data_np[i, j] == -1:
            if curr_num:
                sol -= int(curr_num)
                curr_num = ""
        else:
            curr_num += str(data_np[i, j])

print(f"sol: {sol}")
