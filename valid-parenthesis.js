// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.


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