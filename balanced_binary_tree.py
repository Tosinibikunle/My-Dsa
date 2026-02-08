class Solution:
    def helper(self, root):
        if not root:
            return 0

        left_height = self.helper(root.left)
        if left_height == -1:
            return -1

        right_height = self.helper(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        return self.helper(root) != -1
