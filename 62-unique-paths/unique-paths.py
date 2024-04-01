class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m==1 or n==1:
        #     return 1
        # r=self.uniquePaths(m,n-1)
        # d=self.uniquePaths(m-1,n)
        # return r+d
        DP = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                DP[i][j]=DP[i+1][j]+DP[i][j+1]
        return DP[0][0]
        