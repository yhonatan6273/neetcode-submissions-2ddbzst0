class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        res=0
        while i<j:
            cur_len=j-i
            cur_min=min(heights[i],heights[j])
            res=max(cur_len*cur_min,res)
            if cur_min==heights[i]:
                i+=1
            else:
                j-=1
        return res

        