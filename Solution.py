from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        length = len(s)
        char_map = defaultdict(set)
        for i in range(length):
            char_map[s[i]].add(t[i])
        return not any([(len(val) != 1) for val in char_map.values()])


if __name__ == "__main__":
    s = "egg"
    t = "add"
    sol = Solution()
    print(sol.isIsomorphic(s, t))
