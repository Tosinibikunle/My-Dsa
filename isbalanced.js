function isBalanced(root) {
      function check(node) {
          if (!node) return [true, 0];

              const [leftBalanced, leftHeight] = check(node.left);
                  const [rightBalanced, rightHeight] = check(node.right);

                      const balanced = leftBalanced && rightBalanced && Math.abs(leftHeight - rightHeight) <= 1;
                          return [balanced, 1 + Math.max(leftHeight, rightHeight)];
                            }

                              return check(root)[0];
                              }
