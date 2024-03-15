class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies=0
        res = []
        for candies_i in candies:
            if candies_i> max_candies:
                max_candies=candies_i
        for candies_i in candies:
            if candies_i+extraCandies>=max_candies:
                res += [True]
            else:
                res += [False]    
        return res



        