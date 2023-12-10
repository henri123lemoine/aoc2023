import sys

sol = 0
data = sys.stdin.readlines()
for line in data:
    line = line.strip()
    numbers = [int(x) for x in line.split(" ")]
    differences = []
    differences.append(numbers)
    while True:
        new_numbers = []
        for i in range(len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
        numbers = new_numbers
        differences.append(numbers)
        if all(x == 0 for x in numbers):
            break
    
    differences[-1].insert(0, 0)
    for i in range(len(differences) - 1, 0, -1):
        differences[i - 1].insert(0, differences[i - 1][0] - differences[i][0])
    
    sol += differences[0][0]
    
print(sol)
