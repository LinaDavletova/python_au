class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def Traversal(root):
            if root is None:
                return []
            return Traversal(root.left)+[root.val] + Traversal(root.right)
            
        def iscopy(root):
            if root == []:
                return True
            for i in range(len(root) - 1):
                if root[i] == root[i + 1]:
                    return False
            return True
        return (Traversal(root) == sorted(Traversal(root))) * iscopy(Traversal(root))
