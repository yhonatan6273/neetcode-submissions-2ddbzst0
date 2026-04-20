class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        #הגענו למצב שהמחרוזת ריקה
        dp[0]=True
        i=1
        while i<len(dp):
        
            for word in wordDict:
                lenW=len(word)
                if i>=lenW and s[i-lenW:i]==word:
                    if dp[i-lenW]:
                        dp[i]=True
            i+=1
        return dp[-1]
      
      