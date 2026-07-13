from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in  deadends:
            return -1
        
        q=deque()
        q.append(["0000",0])
        visit=set(deadends)
        def childrens(code):
            res=[]
            for i in range(4):
                digit=str((int(code[i])+1)%10)
                res.append(code[:i]+digit+code[i+1:])
                digit=str((int(code[i])-1+10)%10)
                res.append(code[:i]+digit+code[i+1:])
            return res

        while q:
            code,turn=q.popleft()
            if code==target:
                return turn
            for child in childrens(code):
                if child not in visit:
                    visit.add(child)
                    q.append([child,turn+1])

        return -1


        