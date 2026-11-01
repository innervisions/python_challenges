class Verse:
    def __init__(self, bottles):
        self.bottles = bottles

    def single_verse(self):
        if self.bottles == 0:
            return self._zero_bottle_verse()
        elif self.bottles == 1:
            return self._single_bottle_verse()
        elif self.bottles == 2:
            return self._two_bottle_verse()
        else:
            return self._default_verse()

    def _default_verse(self):
        return (
            f"{self.bottles} bottles of beer on the wall, {self.bottles}"
            f" bottles of beer.\nTake one down and pass it around, "
            f"{self.bottles - 1} bottles of beer on the wall.\n"
        )

    def _two_bottle_verse(self):
        return (
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer "
            "on the wall.\n"
        )

    def _single_bottle_verse(self):
        return (
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer "
            "on the wall.\n"
        )

    def _zero_bottle_verse(self):
        return (
            "No more bottles of beer on the wall, no more bottles "
            "of beer.\nGo to the store and buy some more, 99 bottles "
            "of beer on the wall.\n"
        )

class BeerSong:
    @classmethod
    def verse(cls, number):
        return Verse(number).single_verse()

    @classmethod
    def verses(cls, start, stop):
        result = []
        current_verse = start
        while current_verse >= stop:
            result.append(cls.verse(current_verse))
            current_verse -= 1
        return "\n".join(result)

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)
