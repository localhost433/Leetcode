/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const ret = [];
    for (let i = 0; i < arr.length; i += size) {
        const newArr = arr.slice(i, i + size);
        ret.push(newArr);
    }
    return ret;
};
