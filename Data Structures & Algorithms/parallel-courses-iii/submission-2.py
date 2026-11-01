class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        indegree = [0] * n
        for pre, post in relations:
            adj_list[pre - 1].append(post - 1)
            indegree[post - 1] += 1
        
        init_start = [node for node in range(n) if indegree[node] == 0]

        longest = 0
        while init_start:
            next_node = [init_start.pop()]
            curr_dist = [time[next_node[0]]]
            curr_path = 0
            while next_node:
                curr = next_node.pop()
                dist = curr_dist.pop()
                longest = max(longest, dist)
                curr_path += time[curr]
                next_node.extend(adj_list[curr])
                curr_dist.extend([dist + time[node] for node in adj_list[curr]])

        return longest

