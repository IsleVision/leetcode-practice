class Solution(object):
    def removeStars(self, s):
        i = 0
        res =[]
        while i<len(s):
            if s[i]=='*':
                res.pop()
            else:
                res += [s[i]]
            i+=1
        return ''.join(res)  

        