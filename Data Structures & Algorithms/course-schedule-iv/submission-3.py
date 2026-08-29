class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build collections of all indrect pre reqs then answer in constant time
        # from every node do a DFS and find all nodes that it is a pre req of and store it
        adjList = [[] for _ in range(numCourses)]
        pre_reqs = [set() for _ in range(numCourses)] # for node i a hashset of all its pre reqs
        for c2, c1 in prerequisites:
            adjList[c1].append(c2)
        
        def dfs(i, start):
            #  do DFS to find all courses that are pre reqs of this course
            for nei in adjList[i]:
                if start not in pre_reqs[nei]:
                    pre_reqs[nei].add(start)
                    dfs(nei, start)
            
        for i in range(numCourses):
            dfs(i , i)

        qAns = []
        for c, p in queries:
            ans = p in pre_reqs[c]
            qAns.append(ans)
        
        return qAns