class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        res=0
        if not grid:
            return res

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0":
                return
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for row in range (ROWS):
            for col in range(COLS):
                if grid[row][col]=="1":
                    dfs(row,col)
                    res+=1
        return res


        