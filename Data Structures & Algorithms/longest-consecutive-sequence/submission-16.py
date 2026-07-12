class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=set(nums)
        res=0
        if not nums:
            return res
        for n in nums:
            if n-1 not in numbers:
                length=1
                while n+1 in numbers:
                    length+=1
                    n+=1
                res=max(res,length)

        return res




        