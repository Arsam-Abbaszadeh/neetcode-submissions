class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        self.prefixSums.append(nums[0])
        for i in range(1, len(nums)):
            prev = self.prefixSums[i - 1]
            curr = nums[i]
            self.prefixSums.append(prev + curr)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right] - (self.prefixSums[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)