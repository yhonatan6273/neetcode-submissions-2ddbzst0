import heapq
from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
       
        maxH=[]
        count=Counter(tasks)
        for key,val in count.items():
            maxH.append((-val,key))
        heapq.heapify(maxH)
        time=0
        
        cooldown=deque()
        while maxH or cooldown:
            time+=1
            if cooldown and cooldown[0][1]==time :
               
                    task_info,_=cooldown.popleft()
                    heapq.heappush(maxH,task_info)
                    
                    




            if maxH:
                val,char=heapq.heappop(maxH)
                val=-val
               
                val-=1
                if val!=0:
                    cooldown.append(((-val,char),time+n+1))
            
        return time



