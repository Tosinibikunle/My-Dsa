function missingNumber(nums) {
  const n = nums.length;
  const total = (n * (n + 1)) / 2;
  const sum = nums.reduce((acc, val) => acc + val, 0);
  return total - sum;
}
