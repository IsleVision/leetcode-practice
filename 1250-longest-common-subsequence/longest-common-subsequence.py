class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        DP =[[0 for _ in range(len2)] for _ in range(len1)]
        for i in range(len1):
            for j in range(len2):
                if i==0:
                    if text1[i] in text2[:j+1]:
                        DP[0][j]=1
                    else:
                        DP[0][j]=0
                elif j==0:
                    if text2[j] in text1[:i+1]:
                        DP[i][0]=1
                    else:
                        DP[i][0]=0
                elif text1[i]==text2[j]:
                    DP[i][j]=DP[i-1][j-1]+1
                else:
                    DP[i][j]=max(DP[i-1][j],DP[i][j-1])
        return DP[len1-1][len2-1]



        