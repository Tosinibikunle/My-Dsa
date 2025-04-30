function flatMapArray(arr, callback) {
      return arr.flatMap(callback);
      }

      // Example:
      console.log(flatMapArray([1, 2, 3], x => [x, x * 2]));
      // [1, 2, 2, 4, 3, 6]
