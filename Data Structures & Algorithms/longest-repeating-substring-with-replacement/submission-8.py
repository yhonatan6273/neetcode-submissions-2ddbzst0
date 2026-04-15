from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map=defaultdict(int)
        l,r,cur_max,res=0,0,0,0
        while r<len(s):
            hash_map[s[r]]+=1
            cur_max=max(cur_max,hash_map[s[r]])
            while r-l+1-cur_max>k:
                hash_map[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res


        