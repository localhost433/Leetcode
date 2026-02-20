class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    ret.append(f"{h}:{m:02d}")
        return ret