class MinStack:
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        if not self.stack:
            self.stack.append((val,val))
        else:
            cur_min_val=self.stack[-1][1]
            self.stack.append((val,min(val, cur_min_val)))
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]
        
            