class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        ret = [''] * numRows
        cur = 0
        down = False

        for char in s:
            ret[cur] += char
            if cur == 0 or cur == numRows - 1:
                down = not down
            
            cur += 1 if down else -1

        return "".join(ret)