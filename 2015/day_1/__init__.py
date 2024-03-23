with open("data.txt") as f:
    data = f.read()

def part_1():
    start = 0
    for char in data:
        if char == "(":
            start += 1
        if char == ")":
            start -= 1
    return start
print(part_1())

