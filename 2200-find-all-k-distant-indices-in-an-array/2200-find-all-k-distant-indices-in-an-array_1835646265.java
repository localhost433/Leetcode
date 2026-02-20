class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        int lastCoveredIndex = -1;
        int n = nums.length;
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int L = Math.max(0, i - k);
                int R = Math.min(n - 1, i + k);
                int start = Math.max(L, lastCoveredIndex + 1);
                if (start <= R) {
                    for (int j = start; j <= R; j++) {
                        list.add(j);
                    }
                    lastCoveredIndex = R;
                }

            }
        }
        return list;
    }
}