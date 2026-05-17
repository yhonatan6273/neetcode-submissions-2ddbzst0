class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        Rows=m
        Cols=n
        for r in range(1,Rows):
            for c in range(1,Cols):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]

    