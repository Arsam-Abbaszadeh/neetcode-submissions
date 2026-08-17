class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')        

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)
        else:
            self.stack.append(0)
            self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val
        
    def top(self) -> int:
        return self.min + self.stack[-1] if self.stack[-1] >= 0 else self.min
        

    def getMin(self) -> int:
        return self.min
        
