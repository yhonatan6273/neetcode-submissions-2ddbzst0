class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large,-1*num)
        if (self.small and self.large and  -1*self.large[0]> self.small[0]):
            val=-1*heapq.heappop(self.large)
            heapq.heappush(self.small,val)

        if (len(self.small)>len(self.large)+1):
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if (len(self.large)>len(self.small)+1):
            val=-1*heapq.heappop(self.large)
            heapq.heappush(self.small,val)
        
        

    def findMedian(self) -> float:
        if (len(self.small)>len(self.large)):
            return self.small[0]
        if (len(self.large)>len(self.small)):
            return -1*self.large[0]
        return (self.small[0]+(-1*self.large[0]))/2
        
        