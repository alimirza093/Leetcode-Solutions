# Intersection_of_two_Arrays

# Problem

      # Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Solution

# There are two approches to solve this problem

# Approch 1

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        i , j = 0 , 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] and nums1[i] not in intersection:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return intersection

# Approch 2

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()
#         intersection = set()
#         i , j = 0 , 0
#         Ans = []
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 intersection.add((nums1[i]))
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 i += 1
#         for i in intersection:
#             Ans.append(i)
#         return Ans

