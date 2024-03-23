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

def part_2():
    current_floor = 0
    for index in range(len(data)):
        if data[index] == ")":
            current_floor -= 1
        if data[index] == "(":
            current_floor += 1
        if current_floor == -1:
            return index + 1
print(part_2())
