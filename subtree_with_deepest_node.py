class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            # If left subtree is deeper
            if left_depth > right_depth:
                return (left_node, left_depth + 1)

            # If right subtree is deeper
            if right_depth > left_depth:
                return (right_node, right_depth + 1)

            # Both sides have equal depth
            # Current node is the LCA of deepest nodes
            return (node, left_depth + 1)

        return dfs(root)[0]
