from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        path = set([1])
        cycle = []
        dup_point = None
        has_cycle = set()
        def dfs_cycle(curr, prev):
            nonlocal dup_point

            for n in adj_list[curr]:
                if n != prev:
                    if n in path:
                        # cycle detected
                        dup_point = n
                        cycle.append((curr, n))
                        return True
                    else:
                        path.add(n)
                        if dfs_cycle(n, curr):
                            cycle.append((curr, n))
                            return True
                        path.remove(n)
            return False

        dfs_cycle(1, None)

        for edge in cycle:
            has_cycle.add(edge)
            if edge[0] == dup_point:
                break

        for v1, v2 in reversed(edges):
            if (v1, v2) in has_cycle:
                return [v1, v2]
            if (v2, v1) in has_cycle:
                return [v1, v2]