class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)

        def dfs(char_count, left ,right):
            if char_count == n:
                res.append(part.copy())
            if left >= n or right >= n:
                return

            sub_str = s[left: right + 1] if right + 1 < n else s[left:]
            if sub_str == sub_str[::-1]:
                part.append(sub_str)
                dfs(char_count + (right - left + 1), right + 1, right + 1)
                part.pop()

            dfs(char_count, left, right + 1)


        dfs(0, 0, 0)
        return res