from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_map = defaultdict(list)
        self.val_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append(timestamp)
        self.val_map[(timestamp, key)] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.key_map[key]
        # print(timestamps)
        l, r = 0, len(timestamps) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if timestamps[m] <= timestamp:
                res = m
                l = m + 1
            else:
                r = m - 1
        # print(res)
        return self.val_map[(timestamps[res], key)] if res >= 0 else ''