import sys
data = sys.stdin.readlines()

sol = 0
for i, line in enumerate(data):
    line = line.split(": ")[1]
    line = line.split(" | ")
    line = [l.split(" ") for l in line]
    line = [[l.strip() for l in l] for l in line]
    line = [[int(l) for l in l if l] for l in line]

    winning_numbers, numbers_you_have = line

    round_points = -1
    for winning_number in winning_numbers:
        if winning_number in numbers_you_have:
            round_points += 1
    sol += round(2**round_points)

print(sol)