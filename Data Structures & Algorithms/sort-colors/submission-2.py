class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for n in nums:
            count[n]+=1
        ind,i=0,0
        while ind<len(nums):
            while  count[i]==0:
                i+=1
            nums[ind]=i
            count[i]-=1
            ind+=1
        