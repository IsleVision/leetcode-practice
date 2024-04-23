class StockSpanner:

    def __init__(self):
        self.prices=[]
        

    def next(self, price: int) -> int:
        self.prices+=[price]
        length = len(self.prices)
        for i in range(length-1,-1,-1):
            if self.prices[i]>price:
                return length-1-i
        return length
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)