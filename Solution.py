from typing import Optional

from TreeNode import TreeNode


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def add(this, that):
            if that is None:
                return this
            this.val += that.val
            if this.left:
                this.left += that.left
            elif that.left:
                this.left = that.left
            if this.right:
                this.right += that.right
            elif that.right:
                this.right = that.right
            return this

        TreeNode.__add__ = add
        if not root1:
            return root2
        if not root2:
            return root1
        return root1 + root2
