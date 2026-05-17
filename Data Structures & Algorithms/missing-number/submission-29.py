class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        w_sum=0
        num_sums=sum(nums)
        for i in range(len(nums)+1):
            w_sum+=i
        return w_sum-num_sums