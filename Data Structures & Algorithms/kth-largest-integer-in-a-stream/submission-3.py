class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.topK = nums[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.topK) < self.k or val > self.topK[-1]:
            if len(self.topK) == 0:
                self.topK.append(val)
            else:
                for i in range(len(self.topK)):
                    if val > self.topK[i]:
                        self.topK.insert(i, val)
                        if len(self.topK) > self.k:
                            self.topK.pop()
                        break
            
        return self.topK[-1]
        
