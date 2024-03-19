class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=0
        vs = set()
        for key in dic:
            vs.add(dic[key])
        if len(vs)==len(dic):
            return True
        else:
            return False


