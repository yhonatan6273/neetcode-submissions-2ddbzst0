from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hash_table=defaultdict(list)
        visit=set()
        for l,r in edges:
            hash_table[l].append(r)
            hash_table[r].append(l)
        def dfs(node,prev):
            if node in visit:
                return False
          
            visit.add(node)
            
            for child in hash_table[node]:
                if child==prev:
                    continue
                
                if not dfs(child,node):
                    return False
            return True
        


        return dfs(0,None) and len(visit)==n
           