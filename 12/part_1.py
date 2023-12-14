import sys

def get_num_arrangements(condition_records, contiguous_group_sizes) -> int:
    num_arrangements = 0

    # base case
    if len(contiguous_group_sizes) == 0:
        if any(c == '#' for c in condition_records):
            return 0
        return 1
    
    # recursive case
    i1 = 0
    i2 = contiguous_group_sizes[0]
    while i2 <= len(condition_records) and not (i1-1 >= 0 and condition_records[i1-1] == '#'):
        if any(c == '.' for c in condition_records[i1:i1 + contiguous_group_sizes[0]]):
            pass
        elif i1 + contiguous_group_sizes[0] < len(condition_records) and condition_records[i1 + contiguous_group_sizes[0]] == "#":
            pass
        else:
            if i2 == len(condition_records):
                if len(contiguous_group_sizes) == 1:
                    num_arrangements += 1
                else:
                    pass
            else:
                num_arrangements += get_num_arrangements(condition_records[i2+1:], contiguous_group_sizes[1:])
        
        i1 += 1
        i2 += 1
    
    return num_arrangements

sol = 0
for line in sys.stdin.readlines():
    condition_records, contiguous_group_sizes = line.strip().split()
    num_arrangements = get_num_arrangements(condition_records, list(map(int, contiguous_group_sizes.split(","))))
    sol += num_arrangements
print(sol)