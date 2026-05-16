class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),
                   self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
       
        if len(nums) == 1:
            return nums[0]

        first,secend=0,0
        temp=0
        for i in range(len(nums)):
            secend=max(temp,first+nums[i])
            first=temp
            temp=secend
        return secend
