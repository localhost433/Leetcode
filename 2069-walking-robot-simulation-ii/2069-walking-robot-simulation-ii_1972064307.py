class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = [0, 0]
        self.d = 0
        self.directions = ["East", "North", "West", "South"]
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        perim = 2 * (self.w + self.h) - 4
        num %= perim
        
        if num == 0:
            num = perim

        for _ in range(num):
            if self.d == 0:
                if self.pos[0] + 1 < self.w:
                    self.pos[0] += 1
                else:
                    self.d = 1
                    self.pos[1] += 1
            elif self.d == 1:
                if self.pos[1] + 1 < self.h:
                    self.pos[1] += 1
                else:
                    self.d = 2
                    self.pos[0] -= 1
            elif self.d == 2:
                if self.pos[0] - 1 >= 0:
                    self.pos[0] -= 1
                else:
                    self.d = 3
                    self.pos[1] -= 1
            elif self.d == 3:
                if self.pos[1] - 1 >= 0:
                    self.pos[1] -= 1
                else:
                    self.d = 0
                    self.pos[0] += 1

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        if self.pos == [0, 0]: return "South"
        if self.pos == [self.w - 1, 0]: return "East"
        if self.pos == [self.w - 1, self.h - 1]: return "North"
        if self.pos == [0, self.h - 1]: return "West"
        
        return self.directions[self.d]