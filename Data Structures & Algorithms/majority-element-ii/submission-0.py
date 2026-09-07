class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = Counter(nums)
        threshold = len(nums) // 3
        res = []

        for val, freq in freqMap.items():
            if freq > threshold:
                res.append(val)
        return res
