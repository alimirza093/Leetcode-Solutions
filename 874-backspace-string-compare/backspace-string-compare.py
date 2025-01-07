class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(str):
            stack = []
            for char in str:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return processString(s) == processString(t)