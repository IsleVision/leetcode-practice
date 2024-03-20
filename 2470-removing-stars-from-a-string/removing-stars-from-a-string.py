class Solution(object):
    def removeStars(self, s):
        i = 0
        res =''
        while i<len(s):
            if s[i]=='*':
                res = res[:-1]
            else:
                res += s[i]
            i+=1
        return res  

        