import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R=1,max(piles)
        res=-1
        while L<=R:
            mid=(L+R)//2
            totalSum=0
            for p in piles:
                totalSum+=math.ceil(p/mid)
            if totalSum<=h:
                res=mid
                R=mid-1
            else:
                L=mid+1
        return res

        