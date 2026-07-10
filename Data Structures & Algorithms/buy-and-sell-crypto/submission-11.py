class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
        res=0
        cur_min=prices[0]
        cur_max=prices[0]
        
        for j in range(len(prices)):
            if prices[j]<=cur_min:
                res=max(res,cur_max-cur_min)
                cur_min=prices[j]
                cur_max=prices[j]
            elif prices[j]>=cur_max:
                cur_max=prices[j]
            
            
        return max(res,cur_max-cur_min)


            

                
