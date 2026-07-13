from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                place=ord(c)-ord("a")
                count[place]+=1
            count=tuple(count)
            table[count].append(s)
        res=[]
        for key in table.keys():
            cur_list=table[key]
            res.append(cur_list)
            
        return res

        