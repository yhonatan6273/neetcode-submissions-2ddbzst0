class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        #הגענו למצב שהמחרוזת ריקה
        dp[0]=True
        for i in range(1,len(dp)):
            for word in wordDict:
                lenW=len(word)
                if i>=lenW and s[i-lenW:i]==word:
                    if dp[i-lenW]:
                        dp[i]=True
                        break
        return dp[-1]
      
      