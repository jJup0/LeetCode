"""
Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns
  true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns
  true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements
  (it's guaranteed that at least one element exists when this method is
  called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in
averageO(1) time complexity.

Constraints:
- -2^31 <= val <= 2^31 - 1
- At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.
"""
import random


class RandomizedSet(object):
    """
    Maintain a list of items, and a dictionary of the positions of those items.
    Inserting a value adds it to the end of the list.
    Deleting a value overwrites the index of the value to overwrite with the last value in the list.
      If the value to delete is the last item, just pop it off the list.
    O(1) time complexity for all methods
    O(insert_calls) maximum space complexity
    """

    def __init__(self):
        self.nums: list[int] = []
        self.positions: dict[int, int] = dict()

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.positions[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.positions:
            return False

        # remove val from random set
        last_value = self.nums.pop()
        idx_to_replace = self.positions.pop(val)
        if last_value == val:
            # if val was last item in the list, return early
            return True

        # else overwrite val in the list, and update the pointer of the new value
        self.nums[idx_to_replace] = last_value
        self.positions[last_value] = idx_to_replace
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
