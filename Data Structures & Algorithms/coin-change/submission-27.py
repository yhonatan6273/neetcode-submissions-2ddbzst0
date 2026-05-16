class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt=[float("inf")]*(amount+1)
        opt[0]=0
        for i in range(len(opt)):
            for c in coins:
                cur=opt[i]
                if c>i:
                    continue
                opt[i]=min(opt[i],1+opt[i-c])
        return opt[-1] if opt[-1]!=float("inf") else -1 

        
        