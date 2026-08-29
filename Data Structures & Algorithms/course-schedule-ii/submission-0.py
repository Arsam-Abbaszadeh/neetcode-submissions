class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #  Khans algo
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for c2, c1 in prerequisites:
            adj_list[c1].append(c2)
            indegree[c2] += 1
        
        topSort = []
        q = deque()
        for n, degree in enumerate(indegree):
            if degree == 0:
                q.append(n)

        while q:
            cur = q.popleft()
            topSort.append(cur)
            for nei in adj_list[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return topSort if len(topSort) == numCourses else []


        
