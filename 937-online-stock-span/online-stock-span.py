class StockSpanner:

    # def __init__(self):
    #     self.prices=[]
        

    # def next(self, price: int) -> int:
    #     self.prices+=[price]
    #     length = len(self.prices)
    #     for i in range(length-1,-1,-1):
    #         if self.prices[i]>price:
    #             return length-1-i
    #     return length

    def __init__(self):
        self.mono_stack=[]

    def next(self,price:int) -> int:
        cur_span = 1
        while self.mono_stack and self.mono_stack[-1][0]<=price:
            pre_price,pre_span=self.mono_stack.pop()
            cur_span +=pre_span
        self.mono_stack +=[[price,cur_span]]
        return cur_span

        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)