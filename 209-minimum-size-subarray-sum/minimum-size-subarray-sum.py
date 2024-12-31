class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right = 0
        left = 0
        sums = 0
        ans = float('inf')
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= target:
                ans = min(ans , right - left + 1)
                sums -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0