# Find First Palindromic String in the Array

# Problem

        # Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".A string is palindromic if it reads the same forward and backward.

# Solution

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left = 0
            right = len(word) - 1 
            is_palindrome = True

            while left < right:
                if word[left] != word[right]:
                    is_palindrome = False
                    break
                else:
                    left +=  1
                    right -= 1
            if is_palindrome == True:
                return word
        return ""