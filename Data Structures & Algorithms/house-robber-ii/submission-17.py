class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        if len(nums)==1:
            return nums[0]
        def maxRob(numbers):
            j=0
            i=0
            temp=0
            for n in numbers:
                j=max(i,temp+n)
                temp=i
                i=j
            return j
        return max(maxRob(nums[:-1]),maxRob(nums[1:]))
