class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # khans algorithm
        adjList = [[] for _ in range(n)]
        indegree = [0] * n
        for c1, c2 in relations:
            adjList[c1 - 1].append(c2 - 1)
            indegree[c2 - 1] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
            
        sems = 0
        completed = 0
        while q:
            level = len(q)
            sems += 1
            for _ in range(level):
                cur = q.popleft()
                completed += 1

                for post in adjList[cur]:
                    indegree[post] -= 1
                    if indegree[post] == 0:
                        q.append(post)

        return sems if completed == n else -1
