class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        if not intervals:
            return res
        if len(intervals)==1:
            return intervals
        l=0
        start_l,end_l=intervals[l]
        for r in range(len(intervals)):
            start_r,end_r=intervals[r]
            
            if start_r<=end_l:
                end_l=max(end_r,end_l)
                continue
            else:
                res.append([start_l,end_l])
                l=r
                start_l,end_l=intervals[l]
                continue
        res.append([start_l,end_l])
        return res

                



