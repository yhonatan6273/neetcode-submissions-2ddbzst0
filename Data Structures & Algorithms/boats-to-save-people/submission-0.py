class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        res=0
        if not people:
            return 0
        while i<=j:
            whight=people[i]+people[j]
            
            if whight<=limit:
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
                    

        