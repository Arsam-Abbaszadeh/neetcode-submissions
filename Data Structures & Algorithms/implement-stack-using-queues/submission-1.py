from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        for _ in range(len(self.q1)):
            val = self.q1.popleft()
            self.q2.append(val)
        self.q1.append(x)


    def pop(self) -> int:
        res = self.q1.popleft()
        for _ in range(len(self.q2) - 1):
            val = self.q2.popleft()
            self.q1.append(val)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return res

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()