import numpy as np
import sys
data = sys.stdin.readlines()

sol = 0

def num_adj_nums(data_np, x, y):
    num_adj_nums = 0

    _1, _2, _3 = data_np[x-1, y-1:y+2]
    _4, _, _6 = data_np[x, y-1:y+2]
    _7, _8, _9 = data_np[x+1, y-1:y+2]

    # Top row
    if _1 < 0 and _2 < 0 and _3 < 0:
        pass
    elif _1 >= 0 and _2 >= 0 and _3 >= 0:
        num_adj_nums += 1
    elif _1 >= 0 and _3 >= 0:
        num_adj_nums += 2
    else:
        num_adj_nums += 1
    
    # Middle row
    if _4 >= 0:
        num_adj_nums += 1
    if _6 >= 0:
        num_adj_nums += 1
    
    # Bottom row
    if _7 < 0 and _8 < 0 and _9 < 0:
        pass
    elif _7 >= 0 and _8 >= 0 and _9 >= 0:
        num_adj_nums += 1
    elif _7 >= 0 and _9 >= 0:
        num_adj_nums += 2
    else:
        num_adj_nums += 1

    return num_adj_nums


def find_num(data_np, x, y):
    digits = [data_np[x, y]]
    
    # Find digits to the left
    for i in range(y-1, -1, -1):
        if data_np[x, i] >= 0:
            digits.insert(0, data_np[x, i])
        else:
            break
    
    # Find digits to the right
    for i in range(y+1, data_np.shape[1]):
        if data_np[x, i] >= 0:
            digits.append(data_np[x, i])
        else:
            break
    
    return int("".join([str(d) for d in digits]))


data_lst = []
for i, line in enumerate(data):
    line = line.strip()

    line_lst = []
    for j, char in enumerate(line):
        if char in "0123456789":
            line_lst.append(int(char))
        elif char == "*":
            line_lst.append(-2)
        else:
            line_lst.append(-1)
    data_lst.append(line_lst)

data_np = np.array(data_lst)
data_np = np.pad(data_np, 1, mode='constant', constant_values=-1)
print(data_np)

w, h = data_np.shape

# Find special gears
# If the gear is adjacent to *exactly two* numbers, it is a special gear (-2) else it is a normal gear (-1)
special_gears = []
for i in range(data_np.shape[0]):
    for j in range(data_np.shape[1]):
        if data_np[i, j] == -2:
            if num_adj_nums(data_np, i, j) == 2:
                special_gears.append((i, j))
                print(f"special gear: {i}, {j}")
            else:
                data_np[i, j] = -1
print(data_np)

# Find all the numbers adjacent to special gears
for x, y in special_gears:
    print(f"special gear: {x}, {y}")
    print(data_np[x-1:x+2, y-1:y+2])
    nums = []
    # Top
    if data_np[x-1, y] >= 0:
        nums.append(find_num(data_np, x-1, y))
    else:
        if data_np[x-1, y-1] >= 0:
            nums.append(find_num(data_np, x-1, y-1))
        if data_np[x-1, y+1] >= 0:
            nums.append(find_num(data_np, x-1, y+1))
    
    # Middle
    if data_np[x, y-1] >= 0:
        nums.append(find_num(data_np, x, y-1))
    if data_np[x, y+1] >= 0:
        nums.append(find_num(data_np, x, y+1))
    
    # Bottom
    if data_np[x+1, y] >= 0:
        nums.append(find_num(data_np, x+1, y))
    else:
        if data_np[x+1, y-1] >= 0:
            nums.append(find_num(data_np, x+1, y-1))
        if data_np[x+1, y+1] >= 0:
            nums.append(find_num(data_np, x+1, y+1))

    print(nums)
    assert len(nums) == 2
    sol += nums[0] * nums[1]

print(f"sol: {sol}")
