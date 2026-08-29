class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS approach instead
        adj_list = [[] for _ in range(numCourses)]
        for c2, c1 in prerequisites:
            adj_list[c1].append(c2)

        vis = set()
        path = set()
        topSort = []
        def dfs(i):
            for nei in adj_list[i]:
                if nei not in vis:
                    if nei in path:
                        return False
                    path.add(nei)
                    res = dfs(nei)
                    if not res:
                        return False
                    path.remove(nei)

            vis.add(i)
            topSort.append(i)
            return True

        for j in range(numCourses):
            if j not in vis:
                path.add(j)
                res = dfs(j)
                if not res:
                    break
                path.remove(j)

        return topSort[::-1] if len(topSort) == numCourses else []        