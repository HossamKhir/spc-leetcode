#! /usr/bin/env python3


class Solution:
    MASK = 0x03FF

    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a
        negative = a < 0 and b < 0
        if negative:
            a, b = -a, -b
        while b:
            carry = ((a & b) << 1) & self.MASK
            a ^= b
            b = carry
        a &= self.MASK
        return a * -1 if negative else a


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 2))
    print(sol.getSum(2, 3))
    print(sol.getSum(-1, 1))
    print(sol.getSum(-2, -3))
    print(sol.getSum(-1, 0))
