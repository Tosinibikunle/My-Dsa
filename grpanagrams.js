function groupAnagrams(strs) {
  const map = {};
  for (let str of strs) {
    const key = str.split("").sort().join("");
    map[key] = (map[key] || []).concat(str);
  }
  return Object.values(map);
}
