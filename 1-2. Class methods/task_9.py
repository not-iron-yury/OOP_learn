class Scales:
    def __init__(self):
        self.scales_left = 0
        self.scales_right = 0

    def add_right(self, value: int) -> None:
        self.scales_right += value

    def add_left(self, value: int) -> None:
        self.scales_left += value

    def get_result(self) -> str:
        if self.scales_left != self.scales_right:
            return(('Правая чаша тяжелее', 'Левая чаша тяжелее')[self.scales_left > self.scales_right])
        else:
            return('Весы в равновесии')


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())