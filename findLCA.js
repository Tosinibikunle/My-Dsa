function findLCA(root, p, q) {
      if (!root || root === p || root === q) return root;
        const left = findLCA(root.left, p, q);
          const right = findLCA(root.right, p, q);
            return left && right ? root : (left || right);
            }
