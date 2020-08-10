class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, left, right):
        if left is None and right is None:
            return True
        if (left is None and right is not None) or (left is not None and right is None):
            return False
        if left.val == right.val:
            return self.symmetric(left.right, right.left) and self.symmetric(left.left, right.right)
        else:
            return False
