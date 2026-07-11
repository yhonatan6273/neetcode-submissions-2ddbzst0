from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxHeap=[]
        for char,num in count.items():
            maxHeap.append((-num,char))
        heapq.heapify(maxHeap)
        res=""
        if not s:
            return res
        prev=None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
                
            num,char=heapq.heappop(maxHeap)
            res+=char
            num+=1
                
            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None

           
            if num!=0:
                prev=(num,char)
        return res

            

