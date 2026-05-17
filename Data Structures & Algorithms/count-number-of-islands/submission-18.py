class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        Rows=len(grid)
        Cols=len(grid[0])
        d=collections.deque()
        res=0
        def bfs(r,c):
            d.append((r,c))
            visit.add((r,c))
            while d:
                nr,nc=d.popleft()
                diriections=[[nr+1,nc],[nr-1,nc],[nr,nc+1],[nr,nc-1]]
                for row,col in diriections:
                    if row<0 or col<0 or row==Rows or col==Cols or grid[row][col]=="0" or (row,col) in visit:
                        continue
                    d.append((row,col))
                    visit.add((row,col))
        for r in range (Rows):
            for c in range(Cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    res+=1
                    bfs(r,c)
        return res
