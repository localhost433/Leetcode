/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var n = arr.length;
    var ret = new Array(n);
    for (var i = 0; i < n; i++) {
        ret[i] = fn(arr[i], i);
    }
    return ret;
};