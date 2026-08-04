class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in matching:
                top = stack.pop() if stack else "#"
                if matching[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack