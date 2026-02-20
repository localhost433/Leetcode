import java.util.*;

class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int l = n - k + 1;
        int[] ans = new int[l];
        int[] freq = new int[51];
        for (int i = 0; i < k; i++) {
            freq[nums[i]]++;
        }
        ans[0] = xsum(freq, x);
        for (int i = 1; i < l; i++) {
            int out = nums[i - 1];
            int in = nums[i + k - 1];
            freq[out]--;
            freq[in]++;
            ans[i] = xsum(freq, x);
        }
        return ans;
    }

    private int xsum(int[] freq, int x) {
        int sum = 0;
        boolean[] used = new boolean[51];
        for (int take = 0; take < x; take++) {
            int bestVal = 0, bestFreq = 0;
            for (int v = 1; v < 51; v++) {
                if (!used[v] && freq[v] > 0) {
                    if (freq[v] > bestFreq || (freq[v] == bestFreq && v > bestVal)) {
                        bestFreq = freq[v];
                        bestVal = v;
                    }
                }
            }
            if (bestFreq == 0) break;
            used[bestVal] = true;
            sum += bestVal * bestFreq;
        }
        return sum;
    }
}
