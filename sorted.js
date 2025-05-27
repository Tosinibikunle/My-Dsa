class SortedArray {
      constructor() {
          this.arr = [];
   }

  insert(val) {
      this.arr.push(val);
      this.arr.sort((a, b) => a - b);
        }

  extractMin() {
      return this.arr.shift(); // Removes first (smallest)
        }
    }
}