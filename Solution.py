from TreeNode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        TreeNode.__hash__ = lambda this: hash((this.val, this.left, this.right))
        TreeNode.__eq__ = lambda this, that: hash(this) == hash(that)
        if (root is subRoot) or root == subRoot:
            return True
        queue = deque([root])
        while queue:
            node = queue.pop()
            if not node:
                continue
            if node == subRoot:
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False
