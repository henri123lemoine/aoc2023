import sys
from itertools import permutations
from math import lcm

PATTERN = sys.stdin.readline().strip()
sys.stdin.readline()

_map = {}
data = sys.stdin.readlines()
A_count = 0
starting_nodes = []
ending_nodes = []
for line in data:
    key = line.split(" = (")[0]
    if key.endswith("A"):
        A_count += 1
        starting_nodes.append(key)
    if key.endswith("Z"):
        ending_nodes.append(key)
    l, r = line.split(" = (")[-1].replace(" ", "").replace(")", "").strip().split(",")
    _map[key] = (l, r)

print(starting_nodes, ending_nodes)

def find_distance(starting_node, ending_node, _map):
    sol = 0
    curr = starting_node
    while curr != ending_node:
        next_node = _map[curr][PATTERN[sol % len(PATTERN)] == "R"]
        sol += 1
        curr = next_node
        if sol > 1e6:
            return 1_000_000
    return sol


# For each permutation of starting-point-ending-point link, find out how many steps (if ever) it takes to reach it from the starting point
# Then, for each permutation, find the LCM of the steps for each link, and take the smallest such

lcms = []
for i, permutation in enumerate(permutations(ending_nodes)):
    steps = []
    for j, (starting_node, ending_node) in enumerate(zip(starting_nodes, permutation)):
        dist = find_distance(starting_node, ending_node, _map)
        steps.append(dist)
    
    print(permutation, steps)
    
    # Find the LCM of the steps for each link
    lowest_common_multiple = lcm(*steps)
    lcms.append(lowest_common_multiple)
    print(lowest_common_multiple)

print(lcms)
print(min(lcms))


# This was horrible; the way I got the answer was by running the program, observing the single time the steps contained no 1e6 values, and calculated the lcm for that one by running the code below
from math import lcm
print(lcm(11567, 21251, 12643, 16409, 19099, 14257))
