class PriorityQueue {
      constructor() {
          this.queue = [];
         }

      getParentIndex(i) { return Math.floor((i - 1) / 2); }
      getLeftChildIndex(i) { return 2 * i + 1; }
      getRightChildIndex(i) { return 2 * i + 2; }

      swap(i, j) {
         [this.queue[i], this.queue[j]] = [this.queue[j], this.queue[i]];
  }

      insert(value, priority) {
            const newNode = { value, priority };
            this.queue.push(newNode);
            this.heapifyUp();
     }

                                            heapifyUp() {
                                                let index = this.queue.length - 1;
                                                    while (
                                                          index > 0 &&
                                                                this.queue[this.getParentIndex(index)].priority > this.queue[index].priority
                                                                    ) {
                                                                          this.swap(index, this.getParentIndex(index));
                                                                                index = this.getParentIndex(index);
                                                                                    }
                                                                                      }

                                                                                        extractMin() {
                                                                                            if (this.queue.length === 0) return null;
                                                                                                if (this.queue.length === 1) return this.queue.pop();

                                                                                                    const min = this.queue[0];
                                                                                                        this.queue[0] = this.queue.pop();
                                                                                                            this.heapifyDown();
                                                                                                                return min;
                                                                                                                  }

                                                                                                                    heapifyDown() {
                                                                                                                        let index = 0;
                                                                                                                            const size = this.queue.length;

                                                                                                                                while (this.getLeftChildIndex(index) < size) {
                                                                                                                                      let smallerChildIndex = this.getLeftChildIndex(index);
                                                                                                                                            const rightChildIndex = this.getRightChildIndex(index);

                                                                                                                                                  if (
                                                                                                                                                          rightChildIndex < size &&
                                                                                                                                                                  this.queue[rightChildIndex].priority < this.queue[smallerChildIndex].priority
                                                                                                                                                                        ) {
                                                                                                                                                                                smallerChildIndex = rightChildIndex;
                                                                                                                                                                                      }

                                                                                                                                                                                            if (this.queue[index].priority <= this.queue[smallerChildIndex].priority) break;

                                                                                                                                                                                                  this.swap(index, smallerChildIndex);
                                                                                                                                                                                                        index = smallerChildIndex;
                                                                                                                                                                                                            }
                                                                                                                                                                                                              }

                                                                                                                                                                                                                peek() {
                                                                                                                                                                                                                    return this.queue[0] || null;
                                                                                                                                                                                                                      }

                                                                                                                                                                                                                        isEmpty() {
                                                                                                                                                                                                                            return this.queue.length === 0;
                                                                                                                                                                                                                              }
                                                                                                                                                                                                                              }
const pq = new PriorityQueue();

pq.insert('eat', 3);
pq.insert('code', 1);
pq.insert('sleep', 2);

console.log(pq.extractMin()); // { value: 'code', priority: 1 }
console.log(pq.peek());       // { value: 'sleep', priority: 2 }