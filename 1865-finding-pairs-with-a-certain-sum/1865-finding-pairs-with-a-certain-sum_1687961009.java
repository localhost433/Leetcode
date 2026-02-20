class FindSumPairs {
    private final int[] arr1;
    private final int[] arr2;
    private final Map<Integer,Integer> freq2;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.arr1 = nums1;
        this.arr2 = nums2;
        this.freq2 = new HashMap<>();
        for (int v : arr2) {
            freq2.put(v, freq2.getOrDefault(v, 0) + 1);
        }
    }
    
    public void add(int index, int val) {
        int old = arr2[index];
        int updated = old + val;
        freq2.put(old, freq2.get(old) - 1);
        if (freq2.get(old) == 0) {
            freq2.remove(old);
        }
        arr2[index] = updated;
        freq2.put(updated, freq2.getOrDefault(updated, 0) + 1);
    }
    
    public int count(int tot) {
        int s = 0;
        for (int x : arr1) {
            s += freq2.getOrDefault(tot - x, 0);
        }
        return s;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */