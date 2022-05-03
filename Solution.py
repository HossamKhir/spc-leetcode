from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge cases
        if not n:
            return True
        length = len(flowerbed)
        free = 0
        i = 0
        if length <= 2:
            return not sum(flowerbed) and n == 1
        else:
            if flowerbed[0] == 0:
                free += flowerbed[1] == 0
                i = 1
            if flowerbed[-1] == 0:
                free += flowerbed[-2] == 0
                length -= 1
        while i < length:
            if flowerbed[i] == 0 and i + 2 < length:
                if flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                    free += 1
                    if free >= n:
                        return True
                    i += 1
            i += 1
        return free >= n
