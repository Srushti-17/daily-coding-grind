/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length === 0) {
        return init;
    } 
    accum = init
    for (let i=0; i < nums.length; i++) {
        num = fn(accum,nums[i]);
        accum = num;
    }
    return num;
};
