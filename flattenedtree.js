class FlattenedTree {
      constructor(n) {
          this.n = n;
              this.adj = Array.from({ length: n }, () => []);
                  this.flat = [];
                      this.inTime = Array(n).fill(0);
                          this.outTime = Array(n).fill(0);
                              this.timer = 0;
                                }

                                  addEdge(u, v) {
                                      this.adj[u].push(v);
                                          this.adj[v].push(u);
                                            }

                                              dfs(node, parent) {
                                                  this.inTime[node] = this.timer++;
                                                      this.flat.push(node);
                                                          for (let neighbor of this.adj[node]) {
                                                                if (neighbor !== parent) this.dfs(neighbor, node);
                                                                    }
                                                                        this.outTime[node] = this.timer - 1;
                                                                          }
                                                                          }
