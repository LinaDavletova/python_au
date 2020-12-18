# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root):
            if root is None:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
            
        def max(x, y):
            if x > y:
                return x
            return y
        return depth(root)
