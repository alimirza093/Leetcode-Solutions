class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            maxFreq = max(freq.values())
            curLen = right - left + 1
            if curLen - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res , right - left + 1)
        return res
            

