from typing import List

from Node import Node


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return root
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            [stack.append(child) for child in node.children[::-1]]
        return res
