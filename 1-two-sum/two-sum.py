class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        for i,num in enumerate(nums):
            if target - num in HM:
                return [HM[target - num ] , i]
            else:
                HM[num] = i
        return []