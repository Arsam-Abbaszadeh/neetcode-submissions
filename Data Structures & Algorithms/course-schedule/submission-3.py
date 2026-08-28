class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  Khans algorithm

        # build an adjacency list and incoming edges list
        adj_list = [[] for _ in range(numCourses)]
        in_edges = [0 for _ in range(numCourses)]
        for c2, c1 in prerequisites:
            adj_list[c1].append(c2)
            in_edges[c2] += 1
        
        # get nodes with 0 incoming
        completed = 0
        q = deque()
        for i, in_list in enumerate(in_edges):
            if in_list == 0:
                q.append(i)
                completed += 1
        
        while q:
            cur = q.popleft()
            for child in adj_list[cur]:
                in_edges[child] -= 1
                if in_edges[child] == 0:
                    q.append(child) 
                    completed += 1
        
        return completed == numCourses
            
            


