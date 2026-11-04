class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        nodes_vis = 0
        vis = [False] * n

        def dfs(curr, prev) -> bool:
            nonlocal nodes_vis
            nodes_vis += 1
            vis[curr] = True
            for nei in adj_list[curr]:
                if nei != prev and (vis[nei] or dfs(nei, curr)):
                    return True
            return False

        cycle = dfs(0, -1)
        return not cycle and n == nodes_vis
