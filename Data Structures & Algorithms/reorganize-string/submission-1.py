class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-freq, c] for c, freq in count.items()]
        heapq.heapify(heap)
        resStr = []
        prev = ''
        for _ in range(len(s)):
            added = False
            temp = None
            if heap and heap[0][1] == prev:
                temp = heapq.heappop(heap)
            
            if heap:
                top = heapq.heappop(heap)
                resStr.append(top[1])
                prev = top[1]
                top[0] += 1
                if -top[0] > 0:
                    heapq.heappush(heap, top)
                added = True

            if not added:
                return ''

            if temp:
                heapq.heappush(heap, temp)

        return ''.join(resStr)