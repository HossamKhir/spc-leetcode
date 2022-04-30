from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        sort_count = sorted(count, key=(lambda k: count[k]), reverse=True)
        return sort_count[0]
