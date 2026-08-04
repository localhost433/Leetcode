class RecentCounter:
    def __init__(self):
        self.calls = []
        self.b = 0

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[self.b] < t - 3000:
            self.b += 1
        return len(self.calls) - self.b
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)