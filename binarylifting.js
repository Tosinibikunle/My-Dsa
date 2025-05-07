class Tree {
      constructor(n) {
          this.n = n;
          this.LOG = Math.floor(Math.log2(n)) + 1;
          this.adj = Array.from({ length: n }, () => []);
          this.up = Array.from({ length: n }, () => Array(this.LOG).fill(-1));
          this.depth = Array(n).fill(0);
                   }

          addEdge(u, v) {
            this.adj[u].push(v);
            this.adj[v].push(u);
                              }

          dfs(node, parent) {
              this.up[node][0] = parent;
              for (let i = 1; i < this.LOG; i++) {
                 if (this.up[node][i - 1] !== -1) {
                    this.up[node][i] = this.up[this.up[node][i - 1]][i - 1];
                                   }
                                  }

             for (let neighbor of this.adj[node]) {
                                                                                    if (neighbor !== parent) {
                                                                                            this.depth[neighbor] = this.depth[node] + 1;
                                                                                                    this.dfs(neighbor, node);
                                                                                                          }
                                                                                                              }
                                                                                                                }

                                                                                                                  build(root = 0) {
                                                                                                                      this.dfs(root, -1);
                                                                                                                        }

                                                                                                                          liftNode(node, k) {
                                                                                                                              for (let i = this.LOG - 1; i >= 0; i--) {
                                                                                                                                    if (k >= (1 << i)) {
                                                                                                                                            node = this.up[node][i];
                                                                                                                                                    if (node === -1) break;
                                                                                                                                                            k -= (1 << i);
                                                                                                                                                                  }
                                                                                                                                                                      }
                                                                                                                                                                          return node;
                                                                                                                                                                            }

                                                                                                                                                                              lca(u, v) {
                                                                                                                                                                                  if (this.depth[u] < this.depth[v]) [u, v] = [v, u];

                                                                                                                                                                                      // Bring u up to v’s depth
                                                                                                                                                                                          u = this.liftNode(u, this.depth[u] - this.depth[v]);

                                                                                                                                                                                              if (u === v) return u;

                                                                                                                                                                                                  for (let i = this.LOG - 1; i >= 0; i--) {
                                                                                                                                                                                                        if (this.up[u][i] !== -1 && this.up[u][i] !== this.up[v][i]) {
                                                                                                                                                                                                                u = this.up[u][i];
                                                                                                                                                                                                                        v = this.up[v][i];
                                                                                                                                                                                                                              }
                                                                                                                                                                                                                                  }

                                                                                                                                                                                                                                      return this.up[u][0];
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                        }
