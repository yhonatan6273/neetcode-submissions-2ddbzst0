from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # מכיוון שנגענו במפתח, הוא הופך להכי עדכני (MRU)
        # אנחנו מזיזים אותו לסוף הרשימה המקושרת
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache)==self.capacity:
                self.cache.popitem(last=False)
        self.cache[key]=value
        self.cache.move_to_end(key)