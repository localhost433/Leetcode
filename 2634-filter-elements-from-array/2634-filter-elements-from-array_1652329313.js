/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var filteredArr = new Array();
    for (var i = 0; i < arr.length; i++) {
        var n = fn(arr[i], i);
        if (n) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
};