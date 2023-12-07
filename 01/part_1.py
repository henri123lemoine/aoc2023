import sys
data = sys.stdin.readlines()

sol = 0

for line in data:
    digits = []
    for letter in line:
        if letter.isdigit():
            digits.append(letter)
    sol += int(digits[0] + digits[-1])
print(f"sol: {sol}")