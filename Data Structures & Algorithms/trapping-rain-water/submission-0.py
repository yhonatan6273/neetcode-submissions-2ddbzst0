class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res=0
        i=0
        j=len(height)-1
        max_L=height[0]
        max_R=height[0]
        while i<j:
            if height[j]>=height[i]:
                i+=1
                max_L=max()


        

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                if leftMax - height[l]>0:
                    res += leftMax - height[l]
                leftMax = max(leftMax, height[l])
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res