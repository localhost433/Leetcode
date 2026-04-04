class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        cols = len(encodedText) // rows
        ans = []
        for c in range(cols):
            for i in range(rows):
                if c + i < cols:
                    idx = i * cols + (c + i)
                    ans.append(encodedText[idx])
                else:
                    break
        return "".join(ans).rstrip()