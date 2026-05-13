class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_max=0
        i=0
        j=len(heights)-1
        while (j>=i):
            dis=j-i
            cur_max=max(cur_max,dis*min(heights[i],heights[j]))
            if min(heights[i],heights[j])==heights[i]:
                i+=1
            else:
                j-=1;
        return cur_max