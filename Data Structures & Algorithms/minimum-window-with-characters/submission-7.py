from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float("inf")
        table = Counter(t)
        
        # משתנים לשמירת מיקומי החלון הטוב ביותר במקום לגזור מחרוזת כל רגע
        best_start, best_end = 0, 0
        
        for i in range(len(s)):
            if s[i] in table:
                # שיפור 1: העתקה מהירה מובנית של המילון במקום לולאת איפוס ידנית בסוף
                copy = table.copy()
                j = i
                
                while j < len(s):
                    if s[j] in copy:
                        copy[s[j]] -= 1

                        if copy[s[j]] == 0:
                            del copy[s[j]]

                            if len(copy) == 0:
                                # שיפור 2: שמירת אינדקסים בלבד (פעולה של O(1) במקום O(S))
                                if minLen > j - i + 1:
                                    minLen = j - i + 1
                                    best_start = i
                                    best_end = j + 1
                                break
                    j += 1
                    
        # רק בסוף, אם מצאנו חלון, נגזור אותו פעם אחת ויחידה
        return s[best_start:best_end] if minLen != float("inf") else ""