/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let c0 = 0, c1 = 0, c2 = 0;
    for (let x of nums) {
        if (x === 0) c0++;
        else if (x === 1) c1++;
        else c2++;
    }
    let i = 0;
    while (c0--) nums[i++] = 0;
    while (c1--) nums[i++] = 1;
    while (c2--) nums[i++] = 2;
};