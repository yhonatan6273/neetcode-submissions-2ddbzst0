class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=len(nums)-1
        j=len(nums)-2
        while j>=0:
            if (nums[j]+j>=i):
                i=j
                j-=1   
            else:
                j-=1   
            
        return i==0