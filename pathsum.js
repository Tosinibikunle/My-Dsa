/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {boolean}
 */
const hasPathSum = function(root, sum) {
    if (root === null)
        return false
    if (!root.left && !root.right)
        return root.val === sum

    sum -= root.val

    let result = false

    if (root.left) result = hasPathSum(root.left, sum)
    if (root.right && !result) result = hasPathSum(root.right, sum)

    return result
}