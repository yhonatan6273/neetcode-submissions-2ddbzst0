

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashTable=defaultdict(list)
        for w,n in prerequisites:
          hashTable[n].append(w)
        visit=set()
        def dfs(cour):
            if cour in visit:
                return False
          
            visit.add(cour)
            for w in hashTable[cour]:
                if not dfs(w):
                    return False
            visit.remove(cour)
            
            return True

        for cour in range(numCourses):
            if not dfs(cour):
                return False
        return True



      


