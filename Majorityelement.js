/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const map = new Map();
    const half = Math.round(nums.length / 2);
    
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i]
        
        map[num] = map[num] + 1 || 1;
        
        if(map[num] === half) {
            return num;
        }
    }
};