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
            # for pile in piles:
                # times += [-(pile//-speed)]
                # times += [ceil(pile/speed)]
            # return sum(times)
            return sum(ceil(pile/speed) for pile in piles)
        # piles.sort()
        l,r=1,max(piles)
        while l!=r:
            speed = (l+r)//2
            if resolveTime(piles,speed)>h:
                l=speed+1
            else:
                r=speed
        return l

