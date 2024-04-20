class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt=0
        a_b_c= a or b or c
        while a_b_c>0:
            # a_bit = a%2
            # b_bit = b%2
            # c_bit = c%2
            a_bit = a&1
            b_bit = b&1
            c_bit = c&1
            if c_bit==1 and a_bit==0 and b_bit==0:
                cnt+=1
            elif c_bit==0:
                cnt+=a_bit+b_bit
                # if a_bit==1:
                #     cnt+=1
                # if b_bit==1:
                #     cnt+=1
            # a=a//2
            # b=b//2
            # c=c//2
            a=a>>1
            b=b>>1
            c=c>>1
            a_b_c=a or b or c
        return cnt