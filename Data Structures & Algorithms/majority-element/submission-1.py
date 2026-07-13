class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=nums[0]
        count=1
        for num in nums:
            if count==0:
                res=num
            if num==res:
                count+=1
            else:
                count-=1
        return res
