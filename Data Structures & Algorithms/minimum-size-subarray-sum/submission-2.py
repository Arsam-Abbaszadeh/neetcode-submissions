class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        min_len = n + 1
        window_sum = nums[0]

        while r < n:
            if window_sum >= target:
                min_len = min(min_len, r - l + 1)
                window_sum -= nums[l]
                l += 1
                if l > r:
                    r += 1
                    if r < n: window_sum += nums[r]
            else:
                r += 1
                if r < n: window_sum += nums[r]

        return min_len if min_len <= n else 0

