class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for r in range(len(text1)):
            for c in range(len(text2)):
                if text2[c]==text1[r]:

                    dp[r+1][c+1]=dp[r][c]+1
                else:
                    dp[r+1][c+1]=max(dp[r][c+1],dp[r+1][c])
        return dp[-1][-1]


        