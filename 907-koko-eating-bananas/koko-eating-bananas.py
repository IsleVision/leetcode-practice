class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        # length = len(piles)
        # q = h//length
        # r = h - q*length 
        # if r==0:
        #     return -(piles[-1]//-q)
        # min_h = -(piles[-1]//-(q+1))
        # min_l = -(piles[length-r-1]//-q)
        # return max(min_h,min_l)
        l, r = 1, max(piles)
        
        def isSufficientSpeed(cnt):
            return sum(ceil(i/cnt) for i in piles) <= h

        while l < r:
            m = (l + r)//2
            if isSufficientSpeed(m):
                r = m
            else:
                l = m + 1
                
        return l

