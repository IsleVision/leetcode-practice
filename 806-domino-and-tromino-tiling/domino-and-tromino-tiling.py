class Solution:
    def numTilings(self, n: int) -> int:
        # DP[n]=DP[n-1]*2+DP[n-3]
        if n==1:
            return 1
        if n==2:
            return 2
        DP=[0 for _ in range(n+1)]
        DP[0]=1
        DP[1]=1
        DP[2]=2
        for i in range(3,n+1):
            DP[i]=DP[i-1]*2+DP[i-3]
        return DP[n]%(int(1e9)+7)

        