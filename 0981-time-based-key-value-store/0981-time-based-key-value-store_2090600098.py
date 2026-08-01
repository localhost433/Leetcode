class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        def helper(s: int, n: int, prev: str) -> str:
            if s >= n:
                return prev
            mid = s + (n-s)//2
            v, t = values[mid]
            if t == timestamp:
                return v
            elif t > timestamp:
                return helper(s, mid, prev)
            else:
                return helper(mid + 1, n, v)
        return helper(0, len(values), "")

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)