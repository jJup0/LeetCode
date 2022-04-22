from typing import List, Optional


class MyHashMap:
    # constraints:
    # 0 <= key <= 1_000_000
    # At most 10_000 calls will be made to add, remove, and contains.

    def __init__(self):
        self.mod = 997  # use a prime number for size to make distribution more even
        self.keys: List[Optional[List[int]]] = [None] * self.mod
        self.values: List[Optional[List[int]]] = [None] * self.mod

    def put(self, key: int, value: int) -> None:
        # generate a simple hash of the value by calculating modulo size
        h = key % self.mod

        # get the list of keys for that hash
        keysForHash = self.keys[h]

        # if the list contains values, and the key is not in the list, append it
        if keysForHash:
            if key not in keysForHash:
                keysForHash.append(key)
                assert self.values[h] is not None
                self.values[h].append(value)
            else:
                idx = keysForHash.index(key)
                assert self.values[h] is not None
                self.values[h][idx] = value
        else:
            # else initialize new mapping
            self.keys[h] = [key]
            self.values[h] = [value]

    def get(self, key: int) -> int:
        # get hash of the value
        h = key % self.mod

        # get key list for hash
        keysForHash = self.keys[h]

        # if list exists and key in list, return the mapping
        if keysForHash and (key in keysForHash):
            idx = keysForHash.index(key)
            assert self.values[h] is not None
            return self.values[h][idx]
        else:
            # else return -1
            return -1

    def remove(self, key: int) -> None:
        # get hash of the value
        h = key % self.mod

        # get key list for hash
        keysForHash = self.keys[h]

        # if list exists and key in list, delete the mapping
        if keysForHash and (key in keysForHash):
            idx = keysForHash.index(key)
            keysForHash.pop(idx)
            assert self.values[h] is not None
            self.values[h].pop(idx)
