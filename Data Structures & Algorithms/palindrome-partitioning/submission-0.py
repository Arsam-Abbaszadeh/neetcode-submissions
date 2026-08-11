class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(curr, char_count, left ,right):
            if char_count == n:
                res.append(curr.copy())
            if left >= n or right >= n:
                return

            sub_str = s[left: right + 1] if right + 1 < n else s[left:]
            if sub_str == sub_str[::-1]:
                curr.append(sub_str)
                dfs(curr, char_count + (right - left + 1), right + 1, right + 1)
                curr.pop()

            dfs(curr, char_count, left, right + 1)


        dfs([], 0, 0, 0)
        return res