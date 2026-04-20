class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        #הגענו למצב שהמחרוזת ריקה
        dp[0]=True
        j=1
        i=0
        while j<len(dp):
        
            for word in wordDict:
                lenW=len(word)
                
                if j>=lenW:
                    i=j-lenW
                    if s[i:j]==word and dp[j-lenW]:
                        dp[j]=True
            j+=1
        return dp[-1]
      
      