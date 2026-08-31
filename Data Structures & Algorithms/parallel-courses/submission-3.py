class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for c1, c2 in relations:
            adjList[c1 - 1].append(c2 - 1)
    
        def dfs_cycle_check(cur, vis: set, path: set):
            if cur in path:
                return True # cycle found
            if cur in vis:
                return False # already visited path, no cycle

            path.add(cur)
            for end_node in adjList[cur]:
                if dfs_cycle_check(end_node, vis, path):
                    return True
            path.remove(cur)
            vis.add(cur)
            return False

        # check for cycles
        visited = set()
        for i in range(n):
            if dfs_cycle_check(i, visited, set()):
                return -1
        
        # get longest path, knowing we have a DAG
        past_length = {}
        def dfs_longest_path(cur) -> int:
            if cur in past_length:
                return past_length[cur]
            
            max_length = 1
            for end_node in adjList[cur]:
                length = dfs_longest_path(end_node)
                max_length = max(length + 1, max_length)

            past_length[cur] = max_length
            return max_length

        return max(dfs_longest_path(n) for n in range(n))
