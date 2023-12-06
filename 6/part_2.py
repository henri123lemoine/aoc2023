import sys
data = sys.stdin.readlines()

t = int(data[0].replace("Time:      ", "").replace(" ", "").strip())
d = int(data[1].replace("Distance:  ", "").replace(" ", "").strip())

sol = 0
high = t
while sol < high:
    mid = (sol + high) // 2
    if mid * (t - mid) > d:
        high = mid
    else:
        sol = mid + 1
low = 0
high = t
while low < high:
    mid = (low + high) // 2
    if mid * (t - mid) > d:
        low = mid + 1
    else:
        high = mid
print(low - sol)
