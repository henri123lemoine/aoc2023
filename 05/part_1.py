import sys

def apply_map(seeds, _map):
    for i, seed in enumerate(seeds):
        for destination_range_start, source_range_start, range_length in _map:
            if seed >= source_range_start and seed < source_range_start + range_length:
                seeds[i] = destination_range_start + (seed - source_range_start)
                break
    return seeds

sol = 0

seeds = [int(seed.strip()) for seed in sys.stdin.readline().strip().replace("seeds: ", "").split(" ")]
sys.stdin.readline().strip()

map_count = 7
for _ in range(map_count):
    sys.stdin.readline().strip()
    _map = []
    while (line := sys.stdin.readline().strip()) != "":
        _map.append([int(num.strip()) for num in line.split(" ")])
    seeds = apply_map(seeds, _map)

sol = min(seeds)

print(f"sol: {sol}")
