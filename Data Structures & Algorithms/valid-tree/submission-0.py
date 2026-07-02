class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        adj_list = {}
        for e, e2 in edges:
            if e in adj_list:
                adj_list[e].append(e2)
            else:
                adj_list[e] = [e2]

            if e2 in adj_list:
                adj_list[e2].append(e)
            else:
                adj_list[e2] = [e]
        
        vis_count = 0
        visited = [0] * n

        def dfs(curr, prev) -> bool:
            adj = adj_list[curr]
            for e in adj:
                if e != prev: 
                    if visited[e]:
                            # cycle detected
                        return False
                            
                    visited[e] = 1
                    nonlocal vis_count
                    vis_count += 1

                    if not dfs(e, curr): # early termination
                        return False                        
            return True

        cycle = dfs(0, None)
        return vis_count + 1 == n and cycle