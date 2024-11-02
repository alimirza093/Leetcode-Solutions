# 3Sum

# Problem

        # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Set = set()
        Ans = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    Set.add((nums[i] , nums[j] , nums[k]))
                    k -= 1
                elif total > 0:
                    k -=1
                else:
                    j += 1
        for i in Set:
            Ans.append(i)
        return Ans
