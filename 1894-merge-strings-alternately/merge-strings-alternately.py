class Solution(object):
    def mergeAlternately(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        length = min(length1,length2)
        res = ''
        for i in range(length):
            res += word1[i]+word2[i]
        if length1 > length:
           res += word1[length:]
        if length2 > length:
           res += word2[length:]               
        return res


        