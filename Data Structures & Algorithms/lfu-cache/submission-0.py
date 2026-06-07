from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = {}  # מילון מרכזי: key -> (value, freq)
        self.freqs = defaultdict(OrderedDict)  # מילון תדירויות: freq -> OrderedDict
        self.min_freq = 0  # מעקב אחרי התדירות המינימלית במערכת
    def _update(self, key: int) -> None:
        # 1. שלוף את הערך והתדירות הנוכחית של המפתח
        val, freq = self.vals[key]
        
        # 2. תמחק את המפתח מה-OrderedDict של התדירות הישנה שלו
        self.freqs[freq].pop(key)
        
        # 3. מקרה קצה: אם ה-OrderedDict של התדירות המינימלית התרוקן לחלוטין,
        # זה אומר שהתדירות המינימלית במערכת עלתה ב-1!
        if freq == self.min_freq and not self.freqs[freq]:
            self.min_freq += 1
            
        # 4. תעדכן את המילון המרכזי עם התדירות החדשה (freq + 1)
        self.vals[key] = (val, freq + 1)
        
        # 5. תכניס את המפתח ל-OrderedDict של התדירות החדשה
        # (מכיוון שזה אינסרט חדש, הוא אוטומטית נכנס לסוף ה-OrderedDict כהכי עדכני)
        self.freqs[freq + 1][key] = None
    def get(self, key: int) -> int:
        # אם המפתח לא קיים, מחזירים 1- לפי הדרישה
        if key not in self.vals:
            return -1
            
        # אם הוא קיים, נשתמש בפונקציית העזר כדי לקדם את התדירות שלו
        self._update(key)
        
        # נחזיר את הערך שלו מתוך המילון המרכזי (אינדקס 0 בטאפל)
        return self.vals[key][0]
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
            
        # תרחיש א': המפתח כבר קיים במערכת
        if key in self.vals:
            # נעדכן את הערך שלו במילון המרכזי (נשמור זמנית על התדירות הישנה)
            freq = self.vals[key][1]
            self.vals[key] = (value, freq)
            # נקרא לפונקציית העזר שתקפיץ את התדירות שלו ב-1 ותסדר את ה-OrderedDict
            self._update(key)
            return

        # תרחיש ב': מפתח חדש לחלוטין!
        # 1. אם הגענו לקצה הקיבולת, צריך לפנות מקום
        if len(self.vals) >= self.capacity:
            # ניגש ל-OrderedDict של התדירות הכי נמוכה (self.min_freq)
            # פקודת popitem(last=False) שולפת ב-O(1) את האיבר הראשון (הכי ישן, ה-LRU)
            k, _ = self.freqs[self.min_freq].popitem(last=False)
            # נמחק את האיבר הישן הזה לחלוטין גם מהמילון המרכזי
            self.vals.pop(k)
            
        # 2. הכנסת המפתח החדש למערכת
        # מפתח חדש תמיד מקבל תדירות התחלתית של 1
        self.vals[key] = (value, 1)
        self.freqs[1][key] = None
        # מכיוון שנכנס איבר חדש עם תדירות 1, התדירות המינימלית במערכת היא בוודאות 1
        self.min_freq = 1