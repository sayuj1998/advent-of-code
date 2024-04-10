with open("data.txt") as f:
    data = f.read()

dimensions = [int(num) for lines in data.splitlines() for num in lines.split("x")]
class Rectangle:
    def __init__(self, l: int, w: int, h: int):
        self.data = [l, w, h]

    def wrapping_paper(self) -> int:
        l, w, h = self.data
        surface_area = 2*l*w + 2*w*h + 2*h*l
        side_areas = l*w, w*h, h*l
        smallest_side = min(side_areas)
        total = surface_area + smallest_side
        return total

    def ribbon(self) -> int:
        l, w, h = self.data
        perimeter = 2 * l + w + h - max(l, w, h)
        bow = l * w * h
        total_ribbon = perimeter + bow
        return total_ribbon

total_wrapping = 0
total_ribbon = 0
for index in range(0, len(dimensions), 3):
    gift = Rectangle(*dimensions[index:index+3])
    total_wrapping += gift.wrapping_paper()
    total_ribbon += gift.ribbon()
print(total_wrapping)
print(total_ribbon)



