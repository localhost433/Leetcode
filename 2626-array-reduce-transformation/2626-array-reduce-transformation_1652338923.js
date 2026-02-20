/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var val = init;
    var idx = 0;
    while (idx < nums.length) {
        val = fn(val, nums[idx]);
        idx++;
    }
    return val;
};