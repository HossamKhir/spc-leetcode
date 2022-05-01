class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [1] * n
        i = 2
        while i * i < n:
            if not sieve[i]:
                i += 1
                continue
            for j in range(i * i, n, i):
                sieve[j] = 0
            i += 1
        return sum(sieve[2:])


if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.countPrimes(n))
