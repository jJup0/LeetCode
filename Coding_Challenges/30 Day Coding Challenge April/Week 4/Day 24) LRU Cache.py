from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]     #so that new item is automatically at end
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)