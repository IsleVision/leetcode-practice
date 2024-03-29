class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for e in nums:
            if e not in dic:
                dic[e]=1
            else:
                dic[e]+=1
        for k,v in dic.items():
            if v==1:
                return k
        return -1
