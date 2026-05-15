class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows,Cols=len(board),len(board[0])
        def dfs(row,col,i):
            if(i>=len(word)):
                return True
            elif(row<0 or col<0 or row>=Rows or
            col>=Cols or board[row][col]!=word[i] or board[row][col]=="#"):
                return False
            temp=board[row][col]
            board[row][col]="#"
            res=(dfs(row+1,col,i+1) or dfs(row-1,col,i+1) or
                    dfs(row,col+1,i+1)or dfs(row,col-1,i+1))
            board[row][col]=temp
            return res



        for r in range(Rows):
            for c in range(Cols):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        return False



        