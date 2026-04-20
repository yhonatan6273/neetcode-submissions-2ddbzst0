class Solution:
    def canJump(self, nums: List[int]) -> bool:
        opt=[False]*len(nums)
        opt[-1]=True
        i,j=len(nums)-1,len(nums)-1
        while j>=0:
            if nums[j]+j>=i:
                opt[j]=True
                i=j
            
            j-=1
        return opt[0]
            
            
        