class Solution(object):
    def toDic(self, words):
        dic = {}
        for w in words:
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
        return dic

    def closeStrings(self, word1, word2):
        dic1=self.toDic(word1)
        dic2=self.toDic(word2)
        return set(dic1.keys())==set(dic2.keys()) and sorted(dic1.values())==sorted(dic2.values())