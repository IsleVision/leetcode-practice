class Solution(object):
    def isSubsequence(self, s, t):
        i,j=0,0
        for j in range(len(t)):
            if i<len(s) and t[j]==s[i]:
                i+=1
        if i==len(s):
            return True
        else:
            return False

        