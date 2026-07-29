class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        arr = [0] * 26
        for char in s[:n // 2]:
            arr[ord(char) - 97] += 1
        mid = s[n // 2] if n % 2 else ''
        L = n // 2
        cap = k * (L + 1)

        def comb(a, b):
            b = min(b, a - b)
            res = 1
            for i in range(b):
                res = res * (a - i) // (i + 1)
                if res >= cap:
                    return cap
            return res

        def total(rem):
            res = 1
            for ct in arr:
                if ct:
                    res *= comb(rem, ct)
                    if res >= cap:
                        return cap
                    rem -= ct
            return res

        if total(L) < k:
            return ''

        half = []
        for pos in range(L):
            rem = L - pos
            T = total(rem)
            for i in range(26):
                if not arr[i]:
                    continue
                f = T * arr[i] // rem
                if k > f:
                    k -= f
                else:
                    arr[i] -= 1
                    half.append(chr(i + 97))
                    break
        half = ''.join(half)
        return half + mid + half[::-1]