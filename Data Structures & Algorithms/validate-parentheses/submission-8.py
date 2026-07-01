class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False


        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in "([{ ":
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack