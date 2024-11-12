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