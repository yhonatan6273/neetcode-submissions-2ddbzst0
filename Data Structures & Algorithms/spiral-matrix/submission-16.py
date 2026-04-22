class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        res = []
        # הגדרת הגבולות כאינדקסים חוקיים אחרונים
        L, R = 0, len(matrix[0]) - 1
        UP, DOWN = 0, len(matrix) - 1
        
        # התנאי משתנה ל <= כי הגבולות הם חלק מהטווח שצריך לסרוק
        while L <= R and UP <= DOWN:
            
            # 1. ימינה: רצים מ-L עד R כולל
            for i in range(L, R + 1):
                res.append(matrix[UP][i])
            UP += 1
            
            # 2. למטה: רצים מ-UP עד DOWN כולל
            for i in range(UP, DOWN + 1):
                res.append(matrix[i][R])
            R -= 1
            
            # בדיקת ביטחון: האם הגבולות חצו אחד את השני?
            if not (L <= R and UP <= DOWN):
                break
                
            # 3. שמאלה: הולכים מ-R אחורה עד L כולל
            for i in range(R, L - 1, -1):
                res.append(matrix[DOWN][i])
            DOWN -= 1
            
            # 4. למעלה: הולכים מ-DOWN אחורה עד UP כולל
            for i in range(DOWN, UP - 1, -1):
                res.append(matrix[i][L])
            L += 1
            
        return res