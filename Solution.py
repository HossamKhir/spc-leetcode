class Solution:
    def isHappy(self, n: int) -> bool:
        # edge case
        if n == 1:
            return True
        while n != 1:
            nxt = 0
            while n:
                nxt += (n % 10) ** 2
                n //= 10
            if nxt == 1:
                return True
            if nxt == 4:
                return False
            n = nxt
