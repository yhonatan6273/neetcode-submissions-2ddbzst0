class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows,Cols=len(heights),len(heights[0])
        visitP=set()
        visitA=set()
        res=[]
        def dfs(r,c,visit,prevH):
            if (r<0 or c<0 or r>=Rows or c>=Cols or (r,c) in visit or prevH>heights[r][c]):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])




        for r in range(Rows):
            dfs(r,0,visitP,heights[r][0])
            dfs(r,Cols-1,visitA,heights[r][Cols-1])
        for c in range(Cols):
            dfs(0,c,visitP,heights[0][c])
            dfs(Rows-1,c,visitA,heights[Rows-1][c])
        for r in range (Rows):
            for c in range (Cols):
                if (r,c) in visitP and (r,c) in visitA:
                    res.append([r,c])
        return res


        

       

        






        