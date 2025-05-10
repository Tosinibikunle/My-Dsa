class HLD {
      constructor(n) {
          this.n = n;
              this.adj = Array.from({ length: n }, () => []);
                  this.size = Array(n).fill(0);
                      this.depth = Array(n).fill(0);
                          this.parent = Array(n).fill(-1);
                              this.heavy = Array(n).fill(-1);
                                  this.head = Array(n).fill(0);
                                      this.pos = Array(n).fill(0);
                                          this.currPos = 0;
                                            }

                                              addEdge(u, v) {
                                                  this.adj[u].push(v);
                                                      this.adj[v].push(u);
                                                        }

                                                          dfs(u, p) {
                                                              this.size[u] = 1;
                                                                  let maxSize = 0;

                                                                      for (let v of this.adj[u]) {
                                                                            if (v === p) continue;
                                                                                  this.parent[v] = u;
                                                                                        this.depth[v] = this.depth[u] + 1;
                                                                                              this.dfs(v, u);
                                                                                                    this.size[u] += this.size[v];

                                                                                                          if (this.size[v] > maxSize) {
                                                                                                                  maxSize = this.size[v];
                                                                                                                          this.heavy[u] = v;
                                                                                                                                }
                                                                                                                                    }
                                                                                                                                      }

                                                                                                                                        decompose(u, h) {
                                                                                                                                            this.head[u] = h;
                                                                                                                                                this.pos[u] = this.currPos++;

                                                                                                                                                    if (this.heavy[u] !== -1) {
                                                                                                                                                          this.decompose(this.heavy[u], h);
                                                                                                                                                              }

                                                                                                                                                                  for (let v of this.adj[u]) {
                                                                                                                                                                        if (v !== this.parent[u] && v !== this.heavy[u]) {
                                                                                                                                                                                this.decompose(v, v);
                                                                                                                                                                                      }
                                                                                                                                                                                          }
                                                                                                                                                                                            }

                                                                                                                                                                                              build(root = 0) {
                                                                                                                                                                                                  this.dfs(root, -1);
                                                                                                                                                                                                      this.decompose(root, root);
                                                                                                                                                                                                        }
                                                                                                                                                                                                        }
