class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash_map=collections.defaultdict(list)
        for n1,n2 in edges:
            hash_map[n1].append(n2)
            hash_map[n2].append(n1)
        visit=set()
        def dfs(prev,i):
            
            if i in visit:
                return False
            visit.add(i)
            for nei in hash_map[i]:
                if nei==prev:
                    continue
                
                if not dfs(i,nei):
                    return False
            
            return True
            
            


        
        return dfs(None,0) and len(visit)==n
            
        