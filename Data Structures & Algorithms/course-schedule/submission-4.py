class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for c2, c1 in prerequisites:
            adj_list[c1].append(c2)

        vis = set()
        path = set()

        def dfs(i):
            for n in adj_list[i]:
                if n not in vis:
                    if n in path:
                        # cycle detected or bubbled up
                        return False
                    path.add(n)
                    res = dfs(n)
                    path.remove
                    if not res:
                        return False

            vis.add(i)
            return True
            
        
        for j in range(numCourses):
            if j not in vis:
                path.add(j)
                dfs(j)
                path.remove(j)

        return len(vis) == numCourses