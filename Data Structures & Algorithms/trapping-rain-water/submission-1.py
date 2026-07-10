class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        max_L,max_R=height[l],height[r]
        res=0
        while l<r:
            if max_L<max_R:
                l+=1
                if max_L-height[l]>0:
                    res+=max_L-height[l]
                max_L=max(max_L,height[l])
            else:
                r-=1
                if max_R-height[r]>0:
                    res+=max_R-height[r]
                max_R=max(max_R,height[r])
        return res