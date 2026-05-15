class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=0
        cur_sum=0
        res=nums[0]
        while (i<len(nums)):
            cur_sum+=nums[i]
            if cur_sum<0:
                res=max(res,cur_sum)
                cur_sum=0
            else:
                res=max(res,cur_sum)

            i+=1
           
        return res

            
            

        