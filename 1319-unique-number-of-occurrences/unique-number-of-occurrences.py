class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=0
        if len(set(dic.values()))==len(dic):
            return True
        else:
            return False


