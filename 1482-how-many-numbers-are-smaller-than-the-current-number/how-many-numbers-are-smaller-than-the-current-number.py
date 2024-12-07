class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        nums_to_count = {}

        for  i , num in enumerate(sorted_num):
            if not num in nums_to_count:
                nums_to_count[num] = i
        return [nums_to_count[num] for num in nums]
