class Solution(object):
    def compress(self, chars):
        i =0
        length = len(chars)
        res=''
        for j in range(length):
            if chars[i]!=chars[j]:
                res+= chars[i]
                res+= str(j-i) if j-1>i else ''
                i=j

        if i!=length-1:
            res+= chars[length-2]
            res+= str(length-i) if length-1>i else ''
        else:
            res+= chars[length-1]        

        for i in range(len(res)):
            chars[i]=res[i]

        return len(res)            
