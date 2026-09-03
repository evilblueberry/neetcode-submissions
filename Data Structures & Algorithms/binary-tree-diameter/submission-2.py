# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def diameter(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1

            left = diameter(root.left) + 1
            right = diameter(root.right) + 1

            self.longest = max(left + right, self.longest)

            return max(left, right)

        dummy = diameter(root)
        return self.longest