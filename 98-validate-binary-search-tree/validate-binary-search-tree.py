# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pre(min, node, high):
            if not node:
                return True
            if not min < node.val < high:
                return False
            return pre(min , node.left , node.val) and pre(node.val , node.right , high)

        return pre(float("-inf"), root, float("inf"))
