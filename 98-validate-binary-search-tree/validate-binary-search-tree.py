# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pre(lower , root , upper):
            if not root:
                return True
            if not lower < root.val < upper:
                return False
            return pre(lower , root.left , root.val) and pre(root.val , root.right , upper)
        return pre(float("-inf") , root , float("inf"))
