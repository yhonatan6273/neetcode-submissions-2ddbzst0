from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q=deque()
        min_q=deque()
        res=1
        i=0
        for j in range(len(nums)):
            while max_q and nums[j]>max_q[-1]:
                max_q.pop()
            max_q.append(nums[j])
            while min_q and nums[j]<min_q[-1]:
                min_q.pop()
            min_q.append(nums[j])
            while max_q[0]-min_q[0]>limit:
                if max_q[0]==nums[i]:
                    max_q.popleft()
                if min_q[0]==nums[i]:
                    min_q.popleft()
                i+=1
            res=max(res,j-i+1)
        return res
