import sys
data = sys.stdin.readlines()

sol = 0
for i, line in enumerate(data, start=1):
    line = " ".join(line.split(" ")[2:])
    game = line.split(";")
    game = [g.strip() for g in game]
    game = [g.split(",") for g in game]
    game = [[g.strip() for g in g] for g in game]
    game = [[g.split(" ") for g in g] for g in game]
    game = [[[int(g[0]), g[1]] for g in g] for g in game]
    
    fewest_reds = 0
    fewest_greens = 0
    fewest_blues = 0

    for reveals in game:
        tmp_fewest_reds = 0
        tmp_fewest_greens = 0
        tmp_fewest_blues = 0

        for num, color in reveals:
            if color == "red":
                tmp_fewest_reds += num
            elif color == "green":
                tmp_fewest_greens += num
            elif color == "blue":
                tmp_fewest_blues += num
        
        if tmp_fewest_reds > fewest_reds:
            fewest_reds = tmp_fewest_reds
        if tmp_fewest_greens > fewest_greens:
            fewest_greens = tmp_fewest_greens
        if tmp_fewest_blues > fewest_blues:
            fewest_blues = tmp_fewest_blues
    
    sol += fewest_reds * fewest_greens * fewest_blues

print(sol)