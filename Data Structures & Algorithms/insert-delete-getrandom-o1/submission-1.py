class RandomizedSet:
    def __init__(self):
        self.values = []
        self.value_index = {}

    def insert(self, val: int) -> bool:
        if val in self.value_index:
            return False
        
        self.values.append(val)
        self.value_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_index:
            return False

        rem_idx = self.value_index[val]
        self.values[-1], self.values[rem_idx] = self.values[rem_idx], self.values[-1]
        self.value_index[self.values[rem_idx]] = rem_idx
        self.values.pop()
        del self.value_index[val]

        return True
        

    def getRandom(self) -> int:
        ran_idx = random.randint(0, len(self.values) - 1)
        return self.values[ran_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()