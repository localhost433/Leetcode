class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (index.containsKey(complement)) {
                return new int[] { index.get(complement), i };
            }
            index.put(nums[i], i);
        }
        return new int[0];  // if no solution
    }
}
