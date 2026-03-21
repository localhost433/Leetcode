int findMin(int* nums, int numsSize) {
    int low = 0;
    int high = numsSize - 1;
    if (nums[low] < nums[high]) return nums[low];
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] > nums[high]) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return nums[low];
}