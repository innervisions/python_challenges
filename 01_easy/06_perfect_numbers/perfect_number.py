class PerfectNumber:
    @classmethod
    def classify(cls, value):
        if value < 1:
            raise ValueError("Input must be a positive integer")

        aliquot_sum = cls._aliquot_sum(value)

        if aliquot_sum == value:
            return "perfect"
        if aliquot_sum < value:
            return "deficient"
        return "abundant"

    @staticmethod
    def _aliquot_sum(value): 
        return sum(PerfectNumber._divisors(value))

    @staticmethod
    def _divisors(value):
        divisors = []
        for num in range(1, (value // 2) + 1):
            if value % num == 0:
                divisors.append(num)

        return divisors
