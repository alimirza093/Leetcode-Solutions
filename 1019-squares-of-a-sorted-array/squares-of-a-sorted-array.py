class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for val in nums:
            arr.append(val**2)
        arr.sort()
        return arr