class SegmentTree {
      constructor(arr) {
          this.n = arr.length;
          this.tree = new Array(4 * this.n).fill(0);
          this.build(arr, 0, 0, this.n - 1);
                    }

                     
      build(arr, node, start, end) {
          if (start === end) {
            this.tree[node] = arr[start];
            } else {
          const mid = Math.floor((start + end) / 2);
          this.build(arr, 2 * node + 1, start, mid);
          this.build(arr, 2 * node + 2, mid + 1, end);
          this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];
                                  }
                                      }

          query(node, start, end, l, r) {
             if (r < start || end < l) return 0;
             if (l <= start && end <= r) return this.tree[node];
             const mid = Math.floor((start + end) / 2);
             return this.query(2 * node + 1, start, mid, l, r) +
                                                                                               this.query(2 * node + 2, mid + 1, end, l, r);
                                                                                                 }

                                                                                                   rangeSum(l, r) {
                                                                                                       return this.query(0, 0, this.n - 1, l, r);
                                                                                                         }
                                                                                                         }
