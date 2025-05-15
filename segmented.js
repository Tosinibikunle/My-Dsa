class SegmentTree {
      constructor(arr) {
          this.n = arr.length;
          this.tree = Array(4 * this.n).fill(0);
          this.build(arr, 0, 0, this.n - 1);
         }

      build(arr, node, l, r) {
          if (l === r) {
              this.tree[node] = arr[l];
         } else {
                const mid = Math.floor((l + r) / 2);
                this.build(arr, 2 * node + 1, l, mid);
                this.build(arr, 2 * node + 2, mid + 1, r);
                this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];
               }
                       }

                                                                    query(node, l, r, ql, qr) {
                                                                        if (qr < l || ql > r) return 0;
                                                                            if (ql <= l && r <= qr) return this.tree[node];
                                                                                const mid = Math.floor((l + r) / 2);
                                                                                    return this.query(2 * node + 1, l, mid, ql, qr) + this.query(2 * node + 2, mid + 1, r, ql, qr);
                                                                                      }

                                                                                        update(node, l, r, idx, val) {
                                                                                            if (l === r) {
                                                                                                  this.tree[node] = val;
                                                                                                      } else {
                                                                                                            const mid = Math.floor((l + r) / 2);
                                                                                                                  if (idx <= mid) this.update(2 * node + 1, l, mid, idx, val);
                                                                                                                        else this.update(2 * node + 2, mid + 1, r, idx, val);
                                                                                                                              this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];
                                                                                                                                  }
                                                                                                                                    }

                                                                                                                                      rangeQuery(ql, qr) {
                                                                                                                                          return this.query(0, 0, this.n - 1, ql, qr);
                                                                                                                                            }

                                                                                                                                              pointUpdate(idx, val) {
                                                                                                                                                  this.update(0, 0, this.n - 1, idx, val);
                                                                                                                                                    }
                                                                                                                                                    }
