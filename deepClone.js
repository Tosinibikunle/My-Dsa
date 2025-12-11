function deepClone(obj) {

      return structuredClone(obj);

}

const original = { a: 1, b: new Map([['key', 'value']]) };
const clone = deepClone(original);

console.log(clone);
