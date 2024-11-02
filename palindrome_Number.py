# Palindrom Number    
      
# Problem

         # Given an integer x, return true if x is a palindrome, and false otherwise.

# Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        is_palindrome = True
        while left < right:
            if x[left] != x[right]:
                is_palindrome = False
                break
            else:
                left += 1
                right -= 1
        return is_palindrome