class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict_sym={ '}':'{',']':'[',')':'(' }
        for sym in s:
            if sym in('{' , '[' , '('):
                stack.append(sym)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if dict_sym[sym]!=top:
                    return False
                continue
        return len(stack)==0