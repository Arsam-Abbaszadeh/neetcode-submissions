class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        res = []
        part = -1
        start = 0
        for i, c in enumerate(s):
            part = max(part, last_index[c])
            if i == part:
                res.append(i - start + 1)
                start = i + 1
        return res