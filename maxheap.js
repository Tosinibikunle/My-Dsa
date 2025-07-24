class MaxHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor((i - 1) / 2);
  }
  getLeftChildIndex(i) {
    return 2 * i + 1;
  }
  getRightChildIndex(i) {
    return 2 * i + 2;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (
      index > 0 &&
      this.heap[this.getParentIndex(index)] < this.heap[index]
    ) {
      this.swap(index, this.getParentIndex(index));
      index = this.getParentIndex(index);
    }
  }

  extractMax() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return max;
  }

  heapifyDown() {
    let index = 0;
    const size = this.heap.length;

    while (this.getLeftChildIndex(index) < size) {
      let largerChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);

      if (
        rightChildIndex < size &&
        this.heap[rightChildIndex] > this.heap[largerChildIndex]
      ) {
        largerChildIndex = rightChildIndex;
      }

      if (this.heap[index] >= this.heap[largerChildIndex]) break;

      this.swap(index, largerChildIndex);
      index = largerChildIndex;
    }
  }

  peek() {
    return this.heap[0] || null;
  }

  size() {
    return this.heap.length;
  }
}
const maxHeap = new MaxHeap();

maxHeap.insert(10);
maxHeap.insert(20);
maxHeap.insert(5);
maxHeap.insert(100);

console.log(maxHeap.extractMax()); // 100
console.log(maxHeap.peek()); // 20
