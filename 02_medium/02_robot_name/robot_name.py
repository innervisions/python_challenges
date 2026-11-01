# import random

# class Robot:
#     _taken_names = set()
    
#     def __init__(self):
#         self._name = self._generate_name()

#     @property
#     def name(self):
#         return self._name

#     def _generate_name(self):
#         name = None
#         while True:
#             name = chr(random.randint(65, 90))
#             name += chr(random.randint(65, 90))
#             for _ in range(3):
#                 name += str(random.randint(0, 9))
#             if name not in type(self)._taken_names:
#                 break

#         type(self)._taken_names.add(name)
#         return name

#     def reset(self):
#         type(self)._taken_names.remove(self.name)
#         self._name = self._generate_name()

import random
import string

class Robot:
    _names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            while True:
                potential_name = self._generate_name()
                if potential_name not in Robot._names:
                    break
            self._name = potential_name
            Robot._names.add(self._name)
        return self._name

    def reset(self):
        Robot._names.discard(self._name)
        self._name = None

    def _generate_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
