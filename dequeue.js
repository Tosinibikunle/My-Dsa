class Deque {
      constructor() {
          this.items = [];
            }

              pushFront(item) {
                  this.items.unshift(item);
                    }

                      pushBack(item) {
                          this.items.push(item);
                            }

                              popFront() {
                                  return this.items.shift();
                                    }

                                      popBack() {
                                          return this.items.pop();
                                            }
                                            }
