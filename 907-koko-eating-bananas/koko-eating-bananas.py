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
        def resolveTime(piles:List[int],speed:int)->int:
            times = []
            for pile in piles:
                times += [-(pile//-speed)]
            return sum(times)
        piles.sort()
        l,r=1,piles[-1]
        while r-l>1:
            speed = (l+r)//2
            if resolveTime(piles,speed)>h:
                l=speed
            else:
                r=speed
        return l if resolveTime(piles,l)<=h else r

