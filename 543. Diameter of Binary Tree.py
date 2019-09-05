class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        res = 0
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            res = max(res, self.getDepth(node.left) + self.getDepth(node.right))

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return res

    def getDepth(self, root):
        if root is not None:
            l = self.getDepth(root.left)
            r = self.getDepth(root.right)
            return  max(l, r) + 1
        else:
            return 0
