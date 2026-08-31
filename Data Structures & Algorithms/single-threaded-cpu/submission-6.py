class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(tasks[i][1], tasks[i][0], i) for i in range(len(tasks))]
        tasks.sort(key= lambda t: t[1])
        time = tasks[0][1]
        mheap = []
        i = 0
        taskOrder = []

        while i < len(tasks) or mheap:
            while i < len(tasks) and tasks[i][1] <= time:
                heapq.heappush(mheap, tasks[i])
                i += 1
            
            if mheap:
                task = heapq.heappop(mheap)
                taskOrder.append(task[2])
                time += task[0]
            elif i < len(tasks):
                time = tasks[i][1]
        
        return taskOrder