class Series:
    def __init__(self, digits):
        self.digits = [int(digit) for digit in digits]

    def slices(self, size):
        if size > len(self.digits):
            raise ValueError("Slices can not be larger than the series.")

        return [self.digits[idx : idx + size] for idx in range(len(self.digits) - size + 1)]
