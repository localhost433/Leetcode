int findMin(int* nums, int numSize) {
    int val = 5001;
    for (int i = 0; i < numSize; ++i) {
        if (nums[i] <= val) {
            val = nums[i];
        }
    }
    return val;
}