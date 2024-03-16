class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split(' ')
        length = len(words)
        res = ''
        for i in range(length-1, -1 , -1):
            if words[i]!='':
                res +=words[i]+' '
        return res.strip()



    

        