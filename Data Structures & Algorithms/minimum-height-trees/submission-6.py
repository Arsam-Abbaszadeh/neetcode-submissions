class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        memo = {}


        def dfs(curr, prev):
            curr_max = 0
            for edge in adj_list[curr]:
                if edge != prev:
                    if (curr, edge) in memo:
                        curr_max = max(curr_max, memo[(curr, edge)])
                    else:
                        h = dfs(edge, curr)
                        memo[(curr, edge)] = h
                        curr_max = max(curr_max, h)
            
            return curr_max + 1

        res = []
        min_h = n
        for root in range(n):
            curr_h = dfs(root, None)
            if curr_h < min_h:
                min_h = curr_h
                res = [root]
            elif curr_h == min_h:
                res.append(root)

        return res