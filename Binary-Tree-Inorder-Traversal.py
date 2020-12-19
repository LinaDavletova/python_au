class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def Traversal(root):
            if root is None:
                return []
            return Traversal(root.left) + [root.val] + Traversal(root.right)
        return Traversal(root)
