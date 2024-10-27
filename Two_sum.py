# Two Sum

# Problem

        # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order. 

# Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        for i,num in enumerate(nums):
            if target - num in HM:
                return [HM[target - num ] , i]
            else:
                HM[num] = i
        return []