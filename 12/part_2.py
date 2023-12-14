import sys

def get_num_arrangements_dp(condition_records, contiguous_group_sizes, cache=None) -> int:
    if cache is None:
        cache = {}

    cache_key = (condition_records, tuple(contiguous_group_sizes))
    if cache_key in cache:
        return cache[cache_key]

    num_arrangements = 0

    # Base case
    if len(contiguous_group_sizes) == 0:
        if any(c == '#' for c in condition_records):
            return 0
        return 1
    
    # Recursive case
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
                num_arrangements += get_num_arrangements_dp(condition_records[i2+1:], contiguous_group_sizes[1:], cache)

        i1 += 1
        i2 += 1

    cache[cache_key] = num_arrangements
    return num_arrangements

sol = 0
for line in sys.stdin.readlines():
    condition_records, contiguous_group_sizes = line.strip().split()
    condition_records = (condition_records + "?") * 5
    condition_records = condition_records[:-1]
    contiguous_group_sizes = list(map(int, contiguous_group_sizes.split(","))) * 5  
      
    num_arrangements = get_num_arrangements_dp(condition_records, contiguous_group_sizes)
    sol += num_arrangements
print(sol)
