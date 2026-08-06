class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        val = self.inc.pop()
        if self.inc:
            self.inc[-1] += val
        return self.stack.pop(-1) + val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            i = min(k, len(self.stack)) - 1
            self.inc[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)