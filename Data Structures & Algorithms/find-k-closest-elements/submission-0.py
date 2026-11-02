class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = (0, k-1)
        curr_diff_sum = sum([abs(arr[n] - x) for n in range(k)])
        closest_diff = curr_diff_sum
        l = 0

        for r in range(k, len(arr)):
            curr_diff_sum = curr_diff_sum + abs(arr[r] - x) - abs(arr[l] - x)
            l += 1

            if curr_diff_sum < closest_diff:
                closest = (l, r)
                closest_diff = curr_diff_sum

        start, end = closest
        return arr[start: end + 1]