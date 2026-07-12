class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        if not heights:
            return res
        l=0
        r=len(heights)-1
        while l<r:
            cur_sum=min(heights[l],heights[r])*(r-l)
            res=max(res,cur_sum)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
        