class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=float("-inf")
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum<0:
                cur_sum=0
                continue
            else:
                res=max(res,cur_sum)
        return res if res!=float("-inf")else max(nums) 

        