import random


class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = dict()

    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if not val in self.pos:
            return False

        idx = self.pos[val]
        last = self.nums[-1]

        self.nums[idx] = last       # switch pos of the popped item and last item
        self.pos[last] = idx
        self.nums.pop()  # remove fomr records

        del self.pos[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)
