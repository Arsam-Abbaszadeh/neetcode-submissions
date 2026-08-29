class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = [[] for _ in range(numCourses)]
        for c2, c1 in prerequisites:
            adjList[c1].append(c2)


        def dfs(node, target):
            if node == target:
                return True
            if (node, target) in memo:
                return memo[(node, target)]
            
            for nei in adjList[node]:
                res = dfs(nei, target)
                # cache answers to all DFS calls
                memo[(nei, target)] = res
                if res:
                    return True
            
            return False
        

        qAns = []
        memo = {}
        for c, p in queries:
            ans = dfs(p, c)
            qAns.append(ans)
        return qAns