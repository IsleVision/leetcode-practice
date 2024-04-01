class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        res = []
        for sp in spells:
            i,j=0,length-1
            while i<j:
                m = (i+j)//2
                mul = sp*potions[m]
                if mul==success:
                    j=m
                elif mul>success:
                    j=m-1
                else:
                    i=m+1
            if sp*potions[i]<success:
                res +=[length-i-1]
            else:
                res +=[length-i]
        return res
