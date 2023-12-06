import sys
data = sys.stdin.readlines()

_id_sum = 0
for i, line in enumerate(data, start=1):
    line = " ".join(line.split(" ")[2:])
    game = line.split(";")
    game = [g.strip() for g in game]
    game = [g.split(",") for g in game]
    game = [[g.strip() for g in g] for g in game]
    game = [[g.split(" ") for g in g] for g in game]
    game = [[[int(g[0]), g[1]] for g in g] for g in game]
    
    for reveals in game:
        tmp_red_totals = 0
        tmp_green_totals = 0
        tmp_blue_totals = 0

        for num, color in reveals:
            if color == "red":
                tmp_red_totals += num
            elif color == "green":
                tmp_green_totals += num
            elif color == "blue":
                tmp_blue_totals += num

        if tmp_red_totals > 12 or tmp_green_totals > 13 or tmp_blue_totals > 14:
            _id_sum += i
            break

sol = (i**2 + i) // 2 - _id_sum
print(f"sol: {sol}")