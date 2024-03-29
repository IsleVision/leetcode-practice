class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        res_0 = [0,1]
        res_v = [0,1]
        h_bit= 1 
        while res_v[-1]<n:
            h_bit<<=1
            res_v += [h_bit+x for x in res_v]
            res_0 += [1+x for x in res_0]
        return res_0[0:n+1]




        