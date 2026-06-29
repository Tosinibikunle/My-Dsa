var isValid = function (str) {

  const map = {
    "(": ")",
    "{": "}",
    "[": "]"
  }

  const stack = [];

  for (let i = 0; i < str.length; i++) {
    if (map[str[i]]) {
      stack.push(map[str[i]])
    } else {
      const closing = stack.pop();
      if (closing !== str[i]) return false
    }

  }
  return stack.length === 0;
}
