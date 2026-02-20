import java.util.HashMap;

class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans  = new int[2];
        int k = 0;
        for (int x : nums) {
            int c = map.getOrDefault(x, 0) + 1;
            map.put(x, c);
            if (c == 2) {
                ans[k++] = x;
                if (k == 2) return ans;
            }
        }
        return ans;
    }
}