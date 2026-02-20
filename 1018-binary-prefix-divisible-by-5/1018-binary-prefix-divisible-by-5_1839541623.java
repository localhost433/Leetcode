class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        int run = 0;
        ArrayList<Boolean> ret = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            run = ((run << 1) + nums[i]) % 5;
            ret.add(run==0);
        } return ret;
    }
}