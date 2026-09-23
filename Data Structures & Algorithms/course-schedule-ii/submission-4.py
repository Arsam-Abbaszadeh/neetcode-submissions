class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList  = defaultdict(list)
        for post, pre in prerequisites:
            adjList[pre].append(post)
        
        topSort = []
        vis = set()
        path = set()
        def dfs(node):
            for child in adjList[node]:
                if child not in vis:
                    if child in path:
                        return True
                    path.add(child)
                    res = dfs(child)
                    path.remove(child)
                    if res:
                        return True
            
            vis.add(node)
            topSort.append(node)
            return False
        
        for node in range(numCourses):
            if node not in vis:
                path.add(node)
                res = dfs(node)
                if res:
                    return []
                path.remove(node)
        topSort.reverse()
        return topSort  
        
            
