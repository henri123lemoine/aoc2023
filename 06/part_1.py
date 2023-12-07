import sys
data = sys.stdin.readlines()

sol = 1

times = [int(num.strip()) for num in data[0].replace("Time:      ", "").split("  ") if num != ""]
distances = [int(num.strip()) for num in data[1].replace("Distance:  ", "").split("  ")]

for time, distance in zip(times, distances):
    tmp = 0
    for i in range(time):
        if i * (time - i) > distance:
            tmp += 1
    sol *= tmp

print(sol)
