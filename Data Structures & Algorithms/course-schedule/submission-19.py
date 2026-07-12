from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table=defaultdict(list)
        for i in range(len(prerequisites)):
            wanted,must=prerequisites[i][0],prerequisites[i][1]
            
            table[wanted].append(must)
        courses=set()
        def dfs(wanted):
            if wanted in courses:
                return False
            elif table[wanted]==True:
                return True
            else:
                courses.add(wanted)

            for child in table[wanted]:
                if not dfs(child):
                    return False
            courses.remove(wanted)
            table[wanted]=True
            return True


        for n in range (numCourses):
            if not dfs(n):
                return False
        return True 


        
