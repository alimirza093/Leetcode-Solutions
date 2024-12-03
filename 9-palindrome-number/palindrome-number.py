class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        # is_palindrome = True
        while left < right:
            if x[left] != x[right]:
                # is_palindrome = False
                return False
                # break
            else:
                left += 1
                right -= 1
        return True