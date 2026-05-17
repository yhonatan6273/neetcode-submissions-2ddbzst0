class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        w_sum=sum(range(len(nums) + 1))
        num_sums=sum(nums)
        
        return w_sum-num_sums