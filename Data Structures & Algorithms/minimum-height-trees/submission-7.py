class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node, prev): # return the node to then search for global longest path
            max_len = 0
            end_node = node
            for nei in adj_list[node]:
                if nei != prev:
                    clen, resn = dfs(nei, node)
                    if clen > max_len:
                        max_len = clen
                        end_node = resn

            return max_len + 1, end_node

        def dfs2(node, prev):
            longest = []

            for n in adj_list[node]:
                if n != prev:
                    res = dfs2(n, node)
                    if len(res) > len(longest):
                        longest = res
            return [node] + longest

        _, the_node = dfs(0, None)
        longest_path = dfs2(the_node, None)
        
        mid = len(longest_path) // 2
        res = [longest_path[mid]]
        if len(longest_path) % 2 == 0:
            res.append(longest_path[mid - 1])
        
        return res






