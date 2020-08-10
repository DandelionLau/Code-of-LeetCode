class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.data = []
        self.index = 0
        self.inOrder(self.root)

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            self.data.append(root.val)
            self.inOrder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.data[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index < len(self.data):
            return True
        else:
            return False
