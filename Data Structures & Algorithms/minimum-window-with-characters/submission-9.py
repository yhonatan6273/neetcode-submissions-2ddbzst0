from collections import Counter,defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
            
        # מילון התדרים של מחרוזת המטרה
        table = Counter(t)
        
        # מילון דינמי שיעקוב אחרי התווים בחלון הנוכחי שלנו
        window_counts = defaultdict(int)
        
        # המשתנים שיעזרו לנו לדעת מתי החלון מכיל את כל התווים הדרושים
        required = len(table)  # כמה תווים ייחודיים אנחנו צריכים
        formed = 0             # כמה תווים ייחודיים השלמנו בחלון הנוכחי
        
        minLen = float("inf")
        best_start, best_end = 0, 0
        
        # המצביע השמאלי של החלון
        l = 0
        
        # המצביע הימני (r) רץ קדימה ומרחיב את החלון
        for r in range(len(s)):
            char = s[r]
            
            # אם התו רלוונטי לנו, נוסיף אותו למילון החלון
            if char in table:
                window_counts[char]+=1
                
                # אם הגענו בדיוק לכמות הנדרשת מהתו הזה, נסמן שהשלמנו עוד יעד
                if window_counts[char] == table[char]:
                    formed += 1
            
            # ברגע שהחלון הנוכחי תקף (מכיל את כל מה שצריך), ננסה לצמצם אותו משמאל
            while l <= r and formed == required:
                # עדכון החלון המינימלי
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    best_start = l
                    best_end = r + 1
                
                # התו שאנחנו עומדים לזרוק מהחלון כשנזיז את l ימינה
                left_char = s[l]
                
                if left_char in table:
                    window_counts[left_char] -= 1
                    # אם בעקבות המחיקה חסר לנו מהתו הזה, החלון כבר לא יהיה תקף
                    if window_counts[left_char] < table[left_char]:
                        formed -= 1
                
                # הזזת המצביע השמאלי ימינה כדי להקטין את החלון
                l += 1
                
        return s[best_start:best_end] if minLen != float("inf") else ""