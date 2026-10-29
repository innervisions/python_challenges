class Octal:
    def __init__(self, value):
        self.value = value

    def to_decimal(self):
        if any(char not in "01234567" for char in self.value):
            return 0

        decimal = 0
        for power, digit in enumerate(reversed(self.value)):
            decimal += int(digit) * (8 ** power)

        return decimal
