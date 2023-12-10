import sys

sol = 0
data = sys.stdin.readlines()
for line in data:
    line = line.strip()
    numbers = [int(x) for x in line.split(" ")]
    line_sol = numbers[-1]
    while True:
        new_numbers = []
        for i in range(len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
        numbers = new_numbers
        line_sol += numbers[-1]
        if all(x == 0 for x in numbers):
            break
    sol += line_sol
print(sol)
