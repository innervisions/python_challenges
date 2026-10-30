class SumOfMultiples:
    def __init__(self, *multiples):
        self.multiples = multiples or (3, 5)

    def to(self, limit):
        total = 0

        for number in range(1, limit):
            if any(number % multiple == 0 for multiple in self.multiples):
                total += number

        return total

    @classmethod
    def sum_up_to(cls, limit):
        return cls().to(limit)
