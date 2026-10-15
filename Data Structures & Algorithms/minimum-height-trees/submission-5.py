class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs_furthest(curr, prev):
            longest = 0
            furthest_node = curr
            for nei in adj_list[curr]:
                if nei != prev:
                    path_len, res = dfs_furthest(nei, curr)
                    if res and path_len > longest:
                        furthest_node = res
                        longest = path_len

            return longest + 1, furthest_node
        longest_path, furthest = dfs_furthest(0, -1)
        
        if longest_path != n:
            longest_path, _ = dfs_furthest(furthest, -1)

        if longest_path % 2 == 0:
            middle1 = longest_path // 2
            middle2 = middle1 + 1
        else:
            middle1 = -1
            middle2 = math.ceil(longest_path / 2)

        ans = []

        def middle_nodes(curr, prev, path_len):
            longest = path_len
            
            for nei in adj_list[curr]:
                if nei != prev:
                    can_len = middle_nodes(nei, curr, path_len + 1)
                    if can_len > longest:
                        longest = can_len

            if longest == longest_path and (path_len == middle1 or path_len == middle2):
                ans.append(curr)

            return longest
            
        middle_nodes(furthest, -1, 1)
        return ans