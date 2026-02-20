class Solution {
    public void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;
        while (mid <= high) {
            switch (nums[mid]) {
                case 0:
                    swap(low++, mid++, nums);
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    swap(mid, high--, nums);
                    break;
            }
        }
    }
    public void swap(int i, int j, int[] nums){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}