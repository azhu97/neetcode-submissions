class TimeMap:

    def __init__(self):
        self.time = defaultdict(list) # key : [(timestamp, key)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.time:
            values = self.time[key]
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2
                if values[m][0] <= timestamp:
                    res = values[m][1]
                    l = m + 1
                else:
                    r = m - 1
        return res

        
