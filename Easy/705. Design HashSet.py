class MyHashSet:
    """
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:
        void add(key) Inserts the value key into the HashSet.
        bool contains(key) Returns whether the value key exists in the HashSet or not.
        void remove(key) Removes the value key in the HashSet. If key does not exist
            in the HashSet, do nothing.
    Constraints:
        0 <= key <= 10^6
        At most 10^4 calls will be made to add, remove, and contains.
    """

    def __init__(self):
        self.set = [False] * 1_000_001

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]


class MyHashSet_realistic_implementation:
    # constraints:
    # 0 <= key <= 1_000_000
    # At most 10_000 calls will be made to add, remove, and contains.

    def __init__(self):
        self.mod = 997  # use a prime number for size to make distribution more even
        self.set: list[list[int] | None] = [None] * self.mod

    def add(self, key: int) -> None:
        # generate a simple hash of the value by calculating modulo size
        h = key % self.mod
        # get the list of values at that hash
        l = self.set[h]

        # if the list contains values, and the key is not in the list, append it
        if l:
            if key not in l:
                l.append(key)
        else:
            # else initialize new list
            self.set[h] = [key]

    def remove(self, key: int) -> None:
        # list.remove() raises value error if not present, so check if contained first
        if self.contains(key):
            # if it is, remove the value
            h = key % self.mod
            self.set[h].remove(key)

    def contains(self, key: int) -> bool:
        # calculate the hash
        h = key % self.mod
        # check if there exists a non empty list for that hash, and return true if the value is contained
        return bool(self.set[h] and (key in self.set[h]))
