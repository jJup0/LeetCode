class mySlowStockSpanner:
    def __init__(self):
        self.stack = [(float('inf'), 1)]

    def next(self, price: int) -> int:
        # retVal = 1
        i = len(self.stack) - 1
        # print(price, i, end=' -> ')
        while i >= 0:
            if self.stack[i][0] <= price:
                i -= self.stack[i][1]
            else:
                break
        self.stack.append((price, len(self.stack)-i))
        # print(i,'stacklen',  len(self.stack), self.stack)
        return len(self.stack)-i-1


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        retVal = 1
        while self.stack and self.stack[-1][0] <= price:
            retVal += self.stack.pop()[1]

        self.stack.append([price, retVal])
        return retVal
