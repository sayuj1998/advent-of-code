with open("data.txt") as f:
    data = f.read()

class Building:
    def __init__(self, data: str):
        self.data = data

    def calculate_floor(self) -> int:
        start = 0
        for char in self.data:
            if char == "(":
                start += 1
            elif char == ")":
                start -= 1
        return start
    def basement_position(self)->int:
        current_floor = 0
        for index in range(len(self.data)):
            if data[index] == ")":
                current_floor -= 1
                if current_floor == -1:
                    return index + 1
            elif data[index] == "(":
                current_floor += 1
        return current_floor

building = Building(data)

print(building.calculate_floor())
print(building.basement_position())