from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if not k % length:
            return
        k %= length
        rotated = nums[:-k]
        del nums[:-k]
        nums.extend(rotated)
