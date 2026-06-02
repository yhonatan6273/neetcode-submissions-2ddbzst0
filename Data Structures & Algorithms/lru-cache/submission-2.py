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
        if key in self.cache:
            # אם המפתח קיים, מעדכנים ערך ומזיזים לסוף
           
            self.cache.move_to_end(key)
        else:
            # אם המפתח לא קיים, בודקים אם הגענו למקסימום קיבולת
            if len(self.cache) >= self.capacity:
                # מוחקים את האיבר הראשון (הכי פחות בשימוש - LRU)
                # last=False אומר להוציא מההתחלה (FIFO/LRU) ולא מהסוף
                self.cache.popitem(last=False)
            
            # מכניסים את האיבר החדש לסוף
        self.cache[key] = value