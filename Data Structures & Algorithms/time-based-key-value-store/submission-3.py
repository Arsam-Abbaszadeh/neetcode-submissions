from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.keyToTimeVal = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTimeVal[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.keyToTimeVal[key]
        idx = bisect_right(candidates, timestamp, key= lambda x: x[0])
        if idx == 0: return ''
        
        time, val = candidates[idx - 1]

        return val