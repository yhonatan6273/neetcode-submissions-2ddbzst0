class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((w,v))
        visit=set()
        t=0
        minheap=[(0,k)]
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if (n1 in visit):
                continue
            visit.add(n1)
            t=w1
            for w2,n2 in edges[n1]:
                if not n2 in visit:
                    heapq.heappush(minheap,(w2+w1,n2))
        return t if len(visit)==n else -1

