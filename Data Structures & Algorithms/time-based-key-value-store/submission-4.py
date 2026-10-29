
class TimeMap:
    def __init__(self):
        self.keyToTimeVal = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTimeVal[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.keyToTimeVal[key]
        idx = -1
        l, r = 0, len(candidates) - 1
        while l <= r:
            m = (l + r) // 2
            time, _ = candidates[m]
            if time > timestamp:
                r = m - 1
            else:
                idx = m
                l = m + 1
        if idx == -1: return ''
        _, val = candidates[idx]

        return val