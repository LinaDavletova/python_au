class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                return root
            root.left, root.right = invert(root.right), invert(root.left)
            return root
        return invert(root)
