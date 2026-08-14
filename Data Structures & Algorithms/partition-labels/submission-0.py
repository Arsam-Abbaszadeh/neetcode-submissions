class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # dont end a sub string for as long as a character appears in the future
        res = []
        count = Counter(s)
        zero = 0
        curr_chars = set()
        start = 0
        for i, c in enumerate(s):
            # reset sub str
            if len(curr_chars) > 0 and len(curr_chars) == zero:
                res.append(i - start)
                start = i
                curr_chars = set()
                zero = 0

            curr_chars.add(c)
            count[c] -= 1
            if count[c] == 0:
                zero += 1
            
        if zero > 0:
            res.append(i - start + 1)

        return res

