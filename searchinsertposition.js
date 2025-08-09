/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    const n = nums.length;
    if (target < nums[0]) { return 0; }
    if (target > nums[n - 1]) { return n; }
    let start = 0;
    let end = n - 1;
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        if (target > nums[mid]) { start = (mid + 1); }
        else if (target < nums[mid]) { end = (mid - 1); }
        else return mid;
    }
    return start;
};