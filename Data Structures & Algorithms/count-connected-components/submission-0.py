class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        vis = [0] * n
        # build adj List
        adj_list = [[] for _ in range(n)]
        for v, v2 in edges:
            adj_list[v].append(v2)
            adj_list[v2].append(v)

        # run BFS or DFS
        # imma do BFS
        from collections import deque
        for i in range(n):
            if not vis[i]:
                count += 1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    vis[cur] = 1
                    for v in adj_list[cur]:
                        if not vis[v]:
                            q.append(v)
                
        return count

        