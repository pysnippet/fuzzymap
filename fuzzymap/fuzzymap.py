# Copyright (C) 2022  Artyom Vancyan
# See full copyright notice at __init__.py
from fuzzywuzzy import fuzz


class FuzzyMap(dict):
    """
    FuzzyMap implements a subtype of `dict` with customized descriptors.

    This kind of dictionary returns the value of the exact key  if there is
    such a key. Otherwise, it will return the value of the most similar key
    satisfying the given ratio. The same mechanism works when setting a new
    or replacing an old key in the dictionary.  If the key is not found and
    does  not  match  any of the keys by the given ratio, it returns `None`.
    """

    # set the minimum percent of the
    # diff between the compared keys
    ratio = 60

    def closest_key(self, key):
        """Returns the closest key matched by the given ratio"""

        if len(self):
            # Calculate matching coefficient of each key via fuzz.ratio
            coefficients = {k: fuzz.ratio(k, key) for k in self.keys()}
            matching = max(coefficients, key=lambda k: coefficients[k])
            if coefficients[matching] > self.ratio:
                return matching
        return key

    def __missing__(self, key):
        return super().get(self.closest_key(key))

    def __setitem__(self, key, value):
        super().__setitem__(self.closest_key(key), value)
