class StockSpanner:

    def __init__(self):
        self.stack = [] # (amount, span)

    def next(self, price: int) -> int:
        if self.stack:
            new_span = 1
            while self.stack and price >= self.stack[-1][0]:
                _, span = self.stack.pop()
                new_span += span

            self.stack.append((price, new_span))
            return new_span
        else:
            self.stack.append((price, 1))
            return 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)