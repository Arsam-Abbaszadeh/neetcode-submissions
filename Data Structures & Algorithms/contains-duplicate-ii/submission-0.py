class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # make dicitionary of value to index then loop through checking for that
        index = defaultdict(list)
        for i in range(len(nums)):
            num = nums[i]
            index[num].append(i)
        
        for group in index.values():
            if len(group) > 1:
                for idx in range(len(group) - 1):
                    if group[idx + 1] - group[idx] <= k:
                        return True
        return False
                

