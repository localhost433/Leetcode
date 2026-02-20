class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        suf = [10^5] * n
        sum = 0
        pre[0] = nums[0]
        suf[n-1] = nums[n-1]
        for i in range(1, n, 1):
            pre[i] = max(pre[i-1], nums[i])
        for j in range(n-2, -1, -1):
            suf[j] = min(suf[j+1], nums[j])
        for k in range(1, n-1, 1):
            if pre[k-1] < nums[k] < suf[k+1]:
                sum += 2
            elif nums[k-1] < nums[k] < nums[k+1]:
                sum += 1
        return sum

            