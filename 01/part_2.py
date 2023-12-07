import sys
data = sys.stdin.readlines()

sol = 0
d = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7": 7, "8": 8, "9": 9,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven": 7, "eight": 8, "nine": 9,
    "eno": 1, "owt": 2, "eerht": 3, "ruof": 4, "evif": 5, "xis": 6, "neves": 7, "thgie": 8, "enin": 9,
}

for line in data:
    queue3 = ["p", "p", "p"]
    queue4 = ["p", "p", "p", "p"]
    queue5 = ["p", "p", "p", "p", "p"]

    digit1 = None
    digit2 = None

    # Find first digit
    for letter in line:
        queue3.pop(0)
        queue4.pop(0)
        queue5.pop(0)

        queue3.append(letter)
        queue4.append(letter)
        queue5.append(letter)

        if letter.isdigit():
            digit1 = letter
            break

        if "".join(queue3) in ["one", "two", "six"]:
            digit1 = "".join(queue3)
            break
        elif "".join(queue4) in ["four", "five", "nine"]:
            digit1 = "".join(queue4)
            break
        elif "".join(queue5) in ["three", "seven", "eight"]:
            digit1 = "".join(queue5)
            break
    
    queue3 = ["p", "p", "p"]
    queue4 = ["p", "p", "p", "p"]
    queue5 = ["p", "p", "p", "p", "p"]

    # Find second digit
    for letter in line[::-1]:
        queue3.pop(0)
        queue4.pop(0)
        queue5.pop(0)

        queue3.append(letter)
        queue4.append(letter)
        queue5.append(letter)

        if letter.isdigit():
            digit2 = letter
            break

        if "".join(queue3) in ["eno", "owt", "xis"]:
            digit2 = "".join(queue3)
            break
        elif "".join(queue4) in ["ruof", "evif", "enin"]:
            digit2 = "".join(queue4)
            break
        elif "".join(queue5) in ["eerht", "neves", "thgie"]:
            digit2 = "".join(queue5)
            break
    
    to_add = int(f"{d[digit1]}{d[digit2]}")
    sol += to_add

print(sol)