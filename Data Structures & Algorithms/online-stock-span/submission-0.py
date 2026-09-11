class StockSpanner:

    def __init__(self):
        self.stock_span_stack = []

    def next(self, price: int) -> int:
        # add in the price, but also return the span
        self.stock_span_stack.append(price)
        
        stack_excluding_price = self.stock_span_stack[:-1]
        counter = 1
        while stack_excluding_price and stack_excluding_price[-1] <= price: 
            counter += 1
            stack_excluding_price.pop()
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)