class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows,Cols=len(grid),len(grid[0])
        res=0
        def dfs(r,c):
            if (r<0 or c<0 or r>=Rows or c>= Cols or grid[r][c]=="0"):
                return
            
            grid[r][c]="0"
            dfs(r+1,c) 
            dfs(r-1,c) 
            dfs(r,c+1) 
            dfs(r,c-1) 
            



        for r in range(Rows):
            for c in range (Cols):
                if grid[r][c]=="1":
                    res+=1
                    dfs(r,c)
        return res