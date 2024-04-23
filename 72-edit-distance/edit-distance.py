class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        DP=[[j for j in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1+1):
            DP[i][0]=i
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1]==word2[j-1]:
                    DP[i][j]=DP[i-1][j-1]
                else:
                    DP[i][j]=min(DP[i-1][j-1]+1,DP[i-1][j]+1,DP[i][j-1]+1)
        return DP[len1][len2]