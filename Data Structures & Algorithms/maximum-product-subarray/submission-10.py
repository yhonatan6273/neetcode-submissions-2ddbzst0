class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=1
        cur_min=1
        cur_res=nums[0]
        for i in range (len(nums)):
            number=nums[i]
            temp=cur_max
            
            cur_max=max(number,cur_max*number,cur_min*number)
            cur_min=min(number,temp*number,cur_min*number)
            cur_res=max(cur_max,cur_res)
        return cur_res
        