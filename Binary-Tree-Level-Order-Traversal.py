class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
 
        tree = []
        
        def dfs(node, depth=0):
            if len(tree) <= depth:
                tree.append([])

            tree[depth].append(node.val)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        if root:
            dfs(root)
        
        return tree
