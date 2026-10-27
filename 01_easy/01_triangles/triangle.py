class Triangle:
    def __init__(self, a, b, c):
        self.sides = sorted((a, b, c))

        if not self._is_valid():
            raise ValueError("Invalid triangle lengths")

    def _is_valid(self):
        return self.sides[0] > 0 and self.sides[0] + self.sides[1] > self.sides[2]

    @property
    def kind(self):
        if self.sides[0] == self.sides[1] == self.sides[2]:
            return 'equilateral'
        
        if self.sides[0] == self.sides[1] or self.sides[1] == self.sides[2]:
            return 'isosceles'
        
        return 'scalene'
            