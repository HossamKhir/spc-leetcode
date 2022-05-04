from typing import Optional

from TreeNode import TreeNode


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root.left and not root.right:
            if root.val >= low and root.val <= high:
                return root
            else:
                return None
        while root.val < low or root.val > high:
            if root.val < low:
                root = root.right
            if root.val > high:
                root = root.left
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == low:
                node.left = None
            if node.val == high:
                node.right = None
            while node.left and node.left.val < low:
                node.left = node.left.right
            while node.right and node.right.val > high:
                node.right = node.right.left
            stack.append(node.right)
            stack.append(node.left)
        return root
