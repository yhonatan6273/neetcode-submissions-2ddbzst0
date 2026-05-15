class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])

        def dfs(r, c, i):
            # תנאי עצירה - מצאנו את כל האותיות
            if i == len(word):
                return True
            
            # בדיקת גבולות, התאמת אות, ובדיקה אם כבר ביקרנו (באמצעות None)
            if (r < 0 or c < 0 or r >= Rows or c >= Cols or 
                board[r][c] != word[i]):
                return False

            # סימון ביקור: שומרים את האות המקורית ומרוקנים את התא
            temp = board[r][c]
            board[r][c] = None 

            # ריצה לכל 4 הכיוונים
            # ברגע שאחד מחזיר True, ה-or יפסיק לבדוק את השאר (Short-circuiting)
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))

            # Backtracking: מחזירים את האות למקומה עבור מסלולים אחרים
            board[r][c] = temp
            
            return res

        # נקודת התחלה: מחפשים את האות הראשונה של המילה בלוח
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False