from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows,Cols=len(grid),len(grid[0])
        d=deque()
        res=0
        visits=set()
        
        def bfs(r,c):
            if (r,c) not in visits:
                d.append((r,c))
                visits.add((r,c))
            
            while d:
                cur_row,cur_col=d.popleft()
                dirictions=[[cur_row+1,cur_col],[cur_row-1,cur_col],[cur_row,cur_col+1],[cur_row,cur_col-1]]
                for row,col in dirictions:
                    if(row<0 or col<0 or row>=Rows or col>=Cols or (row,col) in visits or grid[row][col]=="0"):
                        continue
                    d.append((row,col))
                    visits.add((row,col))


        


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]=="1" and (r,c) not in visits:
                    res+=1
                    bfs(r,c)
                    
        return res



        