class Solution:

    BRACKETS = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in s:
            if stack and stack[-1] == self.BRACKETS.get(i, ""):
                stack.pop()
            else:
                stack.append(i)
        return not stack


if __name__ == "__main__":
    solution = Solution()
    s = "()"
    print(solution.isValid(s))
