import sys

PATTERN = sys.stdin.readline().strip()
sys.stdin.readline()

_map = {}
data = sys.stdin.readlines()
for line in data:
    l, r = line.split(" = (")[-1].replace(" ", "").replace(")", "").strip().split(",")
    _map[line.split(" = (")[0]] = (l, r)

sol = 0
curr = "AAA"
while curr != "ZZZ":
    next_node = _map[curr][PATTERN[sol % len(PATTERN)] == "R"]
    sol += 1
    curr = next_node

print(sol)
