class KDNode {
      constructor(point, depth = 0) {
          this.point = point;
              this.left = this.right = null;
                  this.depth = depth;
                    }
                    }

                    class KDTree {
                      constructor() {
                          this.root = null;
                            }

                              insert(point) {
                                  this.root = this._insert(this.root, point, 0);
                                    }

                                      _insert(node, point, depth) {
                                          if (!node) return new KDNode(point, depth);
                                              const axis = depth % 2;
                                                  if (point[axis] < node.point[axis]) {
                                                        node.left = this._insert(node.left, point, depth + 1);
                                                            } else {
                                                                  node.right = this._insert(node.right, point, depth + 1);
                                                                      }
                                                                          return node;
                                                                            }

                                                                              search(point) {
                                                                                  return this._search(this.root, point, 0);
                                                                                    }

                                                                                      _search(node, point, depth) {
                                                                                          if (!node) return false;
                                                                                              if (node.point[0] === point[0] && node.point[1] === point[1]) return true;
                                                                                                  const axis = depth % 2;
                                                                                                      if (point[axis] < node.point[axis]) {
                                                                                                            return this._search(node.left, point, depth + 1);
                                                                                                                } else {
                                                                                                                      return this._search(node.right, point, depth + 1);
                                                                                                                          }
                                                                                                                            }
                                                                                                                            }
