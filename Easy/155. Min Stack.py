class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minRecord=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minRecord:
            if x <= self.minRecord[-1]:
                self.minRecord.append(x)
        else:
            self.minRecord.append(x)
            
    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minRecord[-1]:
            self.minRecord.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minRecord[-1]
