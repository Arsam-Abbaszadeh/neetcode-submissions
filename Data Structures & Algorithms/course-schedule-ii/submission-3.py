class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList  = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for post, pre in prerequisites:
            adjList[pre].append(post)
            inDegree[post] += 1
        
        startCourses = [course for course, degree in enumerate(inDegree) if degree == 0]
        queue = deque(startCourses)
        # vis = set(startCourses)
        order = []

        while queue:
            curr = queue.popleft()
            for child in adjList[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)

            order.append(curr)
            
        return order if len(order) == numCourses else []