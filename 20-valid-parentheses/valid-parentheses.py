class Solution:
    def isValid(self, s: str) -> bool:
        start = "({["
        end = ")}]"
        stack = []
        for val in s:
            if val in start:
                stack.append(val)
            elif val in end:
                if not stack or stack[-1] != start[end.index(val)]:
                    return False
                stack.pop()
        return len(stack) == 0
