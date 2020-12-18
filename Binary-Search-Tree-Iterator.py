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
