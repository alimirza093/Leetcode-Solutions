class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for val in nums:
            arr.append(val * val)
        return sorted(arr)
