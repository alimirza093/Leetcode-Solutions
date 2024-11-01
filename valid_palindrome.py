# Valid Palindrome

# Problem

        # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.Given a string s, return true if it is a palindrome, or false otherwise

# Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]' , "" , s).lower()
        left = 0
        right = len(s) - 1
        is_palindrome = True

        while left < right:
            if s[left] != s[right]:
                is_palindrome = False
                break
            else:
                left += 1
                right -= 1
        return is_palindrome