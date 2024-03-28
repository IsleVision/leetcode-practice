class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        # return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

        res = [0,1,1]
        while len(res)<=n:
            res += [res[-1]+res[-2]+res[-3]]
        return res[-1]

        