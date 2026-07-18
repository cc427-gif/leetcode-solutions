# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if not node.left:
                return right + 1

            if not node.right:
                return left + 1

            return min(left, right) + 1

        return height(root)