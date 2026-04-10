class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sqrt_n = int(n**0.5)
        
        small_q = []
        for l, r, k, v in queries:
            if k > sqrt_n:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                small_q.append((l, r, k, v))

        k_map = defaultdict(lambda: defaultdict(list))
        for l, r, k, v in small_q:
            rem = l % k
            k_map[k][rem].append((l, r, v))

        for k in k_map:
            for rem in k_map[k]:
                v_len = (n - 1 - rem) // k + 1
                diff = [1] * (v_len + 1)
                
                for l, r, v in k_map[k][rem]:
                    start = (l - rem) // k
                    end = (r - rem) // k
                    diff[start] = (diff[start] * v) % MOD
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[end + 1] = (diff[end + 1] * inv_v) % MOD
                
                mult = 1
                for i in range(v_len):
                    mult = (mult * diff[i]) % MOD
                    actual = rem + i * k
                    nums[actual] = (nums[actual] * mult) % MOD

        ret = 0
        for x in nums:
            ret ^= x
        return ret