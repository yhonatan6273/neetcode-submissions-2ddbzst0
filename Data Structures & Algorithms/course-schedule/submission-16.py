from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        Hash_table=defaultdict(list)
       
        for w,n in prerequisites:
            Hash_table[w].append(n)
        def dfs(i):
            if i in visit:
                return False
            if Hash_table[i]==[]:
                return True
            visit.add(i)
            for child in Hash_table[i]:
                if not dfs(child):
                    return False
            visit.remove(i)
            Hash_table[i]=[]
            return True
            

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

