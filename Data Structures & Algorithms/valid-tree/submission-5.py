class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        nodes_vis = 0
        vis = set()

        def dfs(curr, prev) -> bool:
            nonlocal nodes_vis
            nodes_vis += 1
            vis.add(curr)
            for nei in adj_list[curr]:
                if nei != prev and (nei in vis or dfs(nei, curr)):
                    return True
            return False

        cycle = dfs(0, -1)
        return not cycle and n == nodes_vis
