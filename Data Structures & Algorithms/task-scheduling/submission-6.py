from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tabel=Counter(tasks)
        max_heap=[-i for i in tabel.values()]
        heapq.heapify(max_heap)
        q=deque()
        time=0
        while max_heap or q:
            time+=1
            if q and q[0][1]<=time:
                node,_=q.popleft()
                heapq.heappush(max_heap,node)
            if max_heap:
                currend_task=heapq.heappop(max_heap)+1
                if currend_task<0:
                    q.append((currend_task,time+n+1))
            if q and not max_heap:
                time=q[0][1]-1

        return time

        