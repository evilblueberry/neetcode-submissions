class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for r in s: 
            if r == ')':
                if not stack:
                    return False
                l = stack.pop()
                if l != '(':
                    return False
            elif r == '}':
                if not stack:
                    return False
                l = stack.pop()
                if l != '{':
                    return False
            elif r == ']':
                if not stack:
                    return False
                l = stack.pop()
                if l != '[':
                    return False
            else:
                stack.append(r)

        return len(stack) == 0