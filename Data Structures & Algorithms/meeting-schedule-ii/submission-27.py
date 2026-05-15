"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s=sorted(i.start for i in  intervals)
        e=sorted(i.end for i in intervals)
        if not s or not e:
            return 0
        i=j=0
        cur_res=0
        res=1
        
        while (j<len(e) and i<len(s)):
            if(s[i]<e[j]):
                i+=1
                cur_res+=1
            
            else:
                j+=1
                
                cur_res-=1
            res=max(res,cur_res)
        return res

        