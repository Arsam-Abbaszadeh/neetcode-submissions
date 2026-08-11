class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)

        def dfs(left ,right):
            if left >= n or right >= n:
                if left == right:
                    res.append(part.copy())
                return

            sub_str = s[left: right + 1] if right + 1 < n else s[left:]
            if sub_str == sub_str[::-1]:
                part.append(sub_str)
                dfs(right + 1, right + 1)
                part.pop()

            dfs(left, right + 1)


        dfs(0, 0)
        return res