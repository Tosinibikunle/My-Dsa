class HashTable {
      constructor(size = 42) {
          this.buckets = new Array(size);
    }

      hash(key) {
        return key.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0) % this.buckets.length;
           }

      set(key, value) {
        const index = this.hash(key);
        if (!this.buckets[index]) {
           this.buckets[index] = [];
            }
     this.buckets[index].push([key, value]);
              }

      get(key) {
        const index = this.hash(key);
        const bucket = this.buckets[index];
        if (!bucket) return undefined;

     for (let [k, v] of bucket) {
        if (k === key) return v;
             }
           }
    }
