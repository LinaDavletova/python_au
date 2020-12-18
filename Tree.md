# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
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
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    def Traversal(root):
        if root is None:
            return []
        return Traversal(root.left) + [root.val] + Traversal(root.right)
    return Traversal(root)
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    def invert(root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        root.left, root.right = invert(root.right), invert(root.left)
        return root
    return invert(root)
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.processTree(root)

    def processTree(self, root):
        if root is None:
            return
        self.processTree(root.right)
        self.stack.append(root.val)
        self.processTree(root.left)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) != 0
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
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
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
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
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
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
    return (Traversal(root) == sorted(Traversal(root))) * iscopy(Traversal(root))ree)[k-1]
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
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
```

