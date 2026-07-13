
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=[0]*(max(people)+1)
        for p in people:
            count[p]+=1

        idx,i=0,1
        while idx<len(people):
            while count[i]==0:
                i+=1
            people[idx]=i
            count[i]-=1
            idx+=1
        i=0
        j=len(people)-1
        res=0
        if not people:
            return 0
        while i<=j:
            weight=people[i]+people[j]
            
            if weight<=limit:
                res+=1
                i+=1
                j-=1
            else:
                if people[i]>=people[j]:
                    
                    i+=1
                else:
                    j-=1
                res+=1
        return res
                    

        