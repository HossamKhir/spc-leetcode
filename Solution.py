from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))
        mid_index = length // 2  # + (length % 2)
        return TreeNode(
            nums[mid_index],
            self.sortedArrayToBST(nums[:mid_index]),
            self.sortedArrayToBST(nums[mid_index + 1 :]),
        )
