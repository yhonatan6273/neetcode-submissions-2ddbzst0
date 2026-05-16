class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. נסדר את ה-edges שיהיו (weight, node) כמו ב-Heap
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v)) # עכשיו זה (משקל, יעד)
            
        minHeap = [(0, k)] # (זמן מצטבר, צומת)
        visit = set()
        t = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for w2, n2 in edges[n1]: # עכשיו הסדר פה זהה ל-Heap!
             
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    
        return t if len(visit) == n else -1