class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)==1:
            return 0
        buy=prices[0]
        sell=0
        res =0
        for pr in prices:
            if pr+fee<=sell:
                if sell>buy+fee:
                    res+=sell-buy-fee
                buy=pr
                sell=0
            elif pr<buy:
                buy=pr
            elif pr>sell:
                sell=pr
        if sell!=0 and sell>buy+fee:
            res+=sell-buy-fee
        return res
        