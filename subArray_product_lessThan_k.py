# Subarray Product Less Than K

# Problem

        # Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Solution

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 1:
            return 0
        product = 1
        res = 0
        left = 0
        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            res += right - left + 1
        return res 