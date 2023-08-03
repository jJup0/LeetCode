from typing import List


class Solution:

    """
    Given a string containing digits from 2-9 inclusive, return all possible letter
    combinations that the number could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given
    below. Note that 1 does not map to any letters.

    https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

    Constraints:
        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9']
    """

    def __init__(self):
        # define a mapping from numbers to possible letters
        self.num2let = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        # if the string is empty, return empty list
        if not digits:
            return []

        # combs contains all possible versions of letterCombinations so far
        combs = list(self.num2let[digits[0]])

        # go through rest of the letters, appending them to the previous combinations
        for char in digits[1:]:
            # store new combinations in separate list
            new_combs: list[str] = []
            # iterate through possible letters
            for char in self.num2let[char]:
                # extends new_combs by possible iterators
                new_combs.extend(comb + char for comb in combs)
            # overwrite old combinations
            combs = new_combs

        return combs
