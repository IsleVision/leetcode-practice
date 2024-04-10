class Solution:
    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #     ans = []
    #     def search(start:int, k:int, n:int, res: List[int]):
    #         nonlocal ans
    #         if n<1:
    #             return
    #         if k==1:
    #             if n<start:
    #                 return
    #             else:
    #                 print(res)
    #                 res+=[n]
    #                 ans +=[res]
    #                 return
    #         for i in range(res[-1]+1,10):
    #             res = res.copy()
    #             res +=[i]
    #             search(i,k-1,n-i,res)
                
    #     for i in range(1,10):
    #         search(i,k-1,n-i,[i])
    #     return ans
            
            
            
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, k, res):
            if k == 0 and target == 0:
                return [[]]
            if k == 0 or target < 0:
                return []
            ans = []
            for i in range(start, 10):
                for combo in backtrack(i+1, target-i, k-1, res):
                    ans.append([i] + combo)
            return ans
        
        return backtrack(1, n, k, [])
