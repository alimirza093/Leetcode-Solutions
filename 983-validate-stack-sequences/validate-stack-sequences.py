class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr = 0
        for val in pushed:
            stack.append(val)
            while stack and ptr < len(pushed) and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1
        return len(stack) == 0