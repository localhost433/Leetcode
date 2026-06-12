class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long ones = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
        ones &= -ones;
        vector<int> rets = {0, 0};
        for (int num : nums) {
            if ((num & ones) == 0) {
                rets[0] ^= num;
            } else {
                rets[1] ^= num;
            }
        }
        return rets;
    }
};