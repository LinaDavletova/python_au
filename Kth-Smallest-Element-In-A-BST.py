class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        tree = []
        
        def dfs(node, depth=0):

            tree.append(node.val)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        if root:
            dfs(root)
        
        return sorted(tree)[k-1]
