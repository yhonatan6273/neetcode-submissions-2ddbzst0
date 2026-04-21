class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start=newInterval[0]
        new_end=newInterval[1]
        res=[]
        for i in range (len(intervals)):
            cur_start=intervals[i][0]
            cur_end=intervals[i][1]
            if new_end<cur_start:
                res.append(newInterval)
                return res+intervals[i:]
            elif new_start>cur_end:
                res.append(intervals[i])
            else:
                newInterval=[min(new_start,cur_start),max(new_end,cur_end)]
                new_start=newInterval[0]
                new_end=newInterval[1]
        res.append(newInterval)
        return res
    

