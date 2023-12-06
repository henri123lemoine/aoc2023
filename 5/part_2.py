import sys
from typing import List, Tuple


def combine_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ranges.sort(key=lambda x: x[0])

    # This function should combine overlapping ranges.
    # Ex: [(1, 5), (3, 8), (10, 15)] -> [(1, 8), (10, 15)]
    seed_ranges = []

    # Combine overlapping seed ranges.
    for seed_start, seed_end in ranges:
        if len(seed_ranges) == 0:
            seed_ranges.append((seed_start, seed_end))
        else:
            last_start, last_end = seed_ranges[-1]
            if seed_start <= last_end:
                seed_ranges[-1] = (last_start, max(last_end, seed_end))
            else:
                seed_ranges.append((seed_start, seed_end))
    
    return seed_ranges


def apply_map(seed_ranges: List[Tuple[int, int]], _map: List[Tuple[Tuple[int, int], int]]) -> List[Tuple[int, int]]:

    seed_ranges_to_add = []

    for (map_start, map_end), to_add in _map:
        seed_ranges.sort(key=lambda x: x[0])

        for i, (seed_start, seed_end) in enumerate(seed_ranges):
            # A few cases: (x->y) denotes a range from x to y.
            # 1. The seed range has no overlap with the source range.
            # Ex: seed range is (79->93), map is (50->60)+30. This will require no changes.
            if seed_end <= map_start or seed_start >= map_end:
                continue
            # 2. The seed range is completely within the source range.
            # Ex: seed range is (79->93), map is (50->100)+30. This will require adding 30 to the seed range.
            elif seed_start >= map_start and seed_end <= map_end:
                seed_ranges[i] = (seed_start + to_add, seed_end + to_add)
            # 3. Partial overlaps. These will require adding extra ranges to the seed_ranges list.
            # 3.1. The map is completely within the seed range.
            # Ex: seed range is (79->93), map is (85->90)+30. This will require splitting (79->93) into (79->85) (unchanged), (85+30->90+30), and (90->93) (unchanged).
            elif seed_start <= map_start and seed_end >= map_end:
                seed_ranges[i] = (seed_start, map_start)
                seed_ranges_to_add.append((map_start + to_add, map_end + to_add))
                seed_ranges_to_add.append((map_end, seed_end))
            # 3.2. The seed range is partially to the right of the source range.
            # Ex: seed range is (79->93), map is (50->85)+30. This will require splitting (79->93) into (79+30->85+30) and (85->93) (unchanged).
            elif seed_start >= map_start and seed_end > map_end:
                seed_ranges[i] = (seed_start + to_add, map_end + to_add)
                seed_ranges_to_add.append((map_end, seed_end))
            # 3.2. The seed range is partially to the left of the source range.
            # Ex: seed range is (79->93), map is (90->100)+30. This will require splitting (79->93) into (79->90) (unchanged) and (90+30->93+30).
            elif seed_start < map_start and seed_end <= map_end:
                seed_ranges[i] = (seed_start, map_start)
                seed_ranges_to_add.append((map_start + to_add, seed_end + to_add))
            else:
                raise Exception(f"Unhandled case: seed range is ({seed_start}->{seed_end}), map is ({map_start}->{map_end})+{to_add}.")
    
    seed_ranges.extend(seed_ranges_to_add)
    seed_ranges = combine_ranges(seed_ranges)
    return seed_ranges

sol = 0

tmp = [int(seed.strip()) for seed in sys.stdin.readline().strip().replace("seeds: ", "").split(" ")]
seed_ranges = [(tmp[i], tmp[i] + tmp[i+1]) for i in range(0, len(tmp), 2)]
seed_ranges.sort(key=lambda x: x[0])
print(f"seed_ranges: {seed_ranges}\n")

sys.stdin.readline().strip()

map_count = 7
for _ in range(map_count):
    sys.stdin.readline().strip()
    _map = []
    while (line := sys.stdin.readline().strip()) != "":
        destination_range_start, source_range_start, range_length = [int(num.strip()) for num in line.split(" ")]
        _map.append(((source_range_start, source_range_start + range_length), destination_range_start - source_range_start))
    _map.sort(key=lambda x: x[0][0])
    seed_ranges = apply_map(seed_ranges, _map)
    print(f"map: {_map}\n")
    print(f"seed_ranges: {seed_ranges}\n")
    seed_ranges.sort(key=lambda x: x[0])
    seed_ranges = combine_ranges(seed_ranges)
    print(f"seed_ranges: {seed_ranges}\n")


sol = float("inf")
for start_range, end_range in seed_ranges:
    sol = min(sol, start_range)

print(f"sol: {sol}")
