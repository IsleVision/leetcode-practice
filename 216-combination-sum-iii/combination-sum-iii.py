class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def search(start:int, k:int, n:int, res: List[int]):
            nonlocal ans
            if n<1:
                return
            if k==1:
                if n<=start or n>9:
                    return
                else:
                    res +=[n]
                    ans +=[res]
                    return
            for i in range(res[-1]+1,10):
                search(i,k-1,n-i,res+[i])
                
        for i in range(1,10):
            search(i,k-1,n-i,[i])
        return ans
            
            
            

