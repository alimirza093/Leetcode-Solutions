# Move Zeros

# Problem

        # Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

# Solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[left] != 0:
                left += 1
                continue
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
        return nums 