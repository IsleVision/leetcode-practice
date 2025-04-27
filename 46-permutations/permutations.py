class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[n] for n in nums]
        res_temp = []
        for _ in range(1,len(nums)):
            res_temp = []
            for r in res:
                for v in set(nums)-set(r):
                    res_temp += [r[:]+[v]]
                res=res_temp
        return res







        