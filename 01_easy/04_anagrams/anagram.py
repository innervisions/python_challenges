class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = list(filter(self._is_anagram, words))
        return anagrams

    def _is_anagram(self, other_word):
        other_word = other_word.lower()

        if self.word == other_word:
            return False

        return sorted(self.word) == sorted(other_word)
