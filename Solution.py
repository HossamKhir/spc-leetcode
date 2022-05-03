from typing import Optional
from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            if node.left or node.right:
                node.left, node.right = node.rigth, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
