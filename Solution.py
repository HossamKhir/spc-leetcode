from typing import List


class Solution:
    LOWER_LIMIT = int(-1e5)
    UPPER_LIMIT = int(1e5)

    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        mods = 0
        i = 0
        lower = self.LOWER_LIMIT
        upper = self.UPPER_LIMIT
        while i < n - 1 and mods <= 1:
            if nums[i + 1] < nums[i]:
                mods += 1
                if nums[i + 1] >= lower:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
            lower = min(upper, nums[i])
            i += 1
        return (i == n - 1) and (mods <= 1)


if __name__ == "__main__":
    # nums = [4, 2, 1]
    nums = [3, 4, 2, 3]
    print(Solution().checkPossibility(nums))
