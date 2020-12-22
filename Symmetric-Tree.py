class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        tree = []
        
        def dfs(node, depth=0):
            if len(tree) <= depth:
                tree.append([])
            tree[depth].append(node.val)
            if node.left is None:
                tree.append([])
                tree[depth+1].append("null")
            elif node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
            elif node.right is None:
                tree[depth+1].append("null")
        if root:
            dfs(root)
            
        def isSymmetric(tree):
            for i in tree:
                for j in range(len(i) // 2):
                    if i[j] != i[len(i) - j - 1]:
                        return False
            return True
        print (tree)
        return isSymmetric(tree)
