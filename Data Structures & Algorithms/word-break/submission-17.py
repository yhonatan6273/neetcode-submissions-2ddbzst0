class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        #הגענו למצב שהמחרוזת ריקה
        dp[0]=True
        j=1
        while j<len(dp):
        
            for word in wordDict:
                lenW=len(word)
                if j>=lenW and s[j-lenW:j]==word:
                    if dp[j-lenW]:
                        dp[j]=True
            j+=1
        return dp[-1]
      
      