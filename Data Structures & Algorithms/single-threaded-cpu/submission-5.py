class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # brute force n^2 time solution
        tasks = [(i, tasks[i][0], tasks[i][1]) for i in range(len(tasks))]
        tasks.sort(key=lambda x: x[2])
        time = 0
        res = []
        while tasks:
            idx = -1
            shortest_time = float('inf')
            for i in range(len(tasks)):
                if tasks[i][1] <= time:
                    idx = i
                    shortest_time = tasks[i][1]
                    break
                elif shortest_time > tasks[i][1]:
                    idx = i
                    shortest_time = tasks[i][1]

            i, enq, pro = tasks.pop(idx)
            time = max(time, enq)
            time += pro
            res.append(i)
        return res