class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp=0
        rob1=0
        rob2=0
        for i in range(len(nums)):
            rob1=max(rob2,nums[i]+temp)
            temp=rob2
            rob2=rob1
        return rob1
            