var findMedianSortedArrays = function(nums1, nums2) {
     var allNums = nums1.concat(nums2);
     allNums = allNums.sort((a, b) => a - b)
     var middleIndex = Math.floor(allNums.length / 2);

          if (allNums.length % 2 === 1) return allNums[middleIndex];
              else return ((allNums[middleIndex - 1] + allNums[middleIndex]) / 2)
              };
