class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = [0]
        self.treeSum(root, res)
        total = res.pop()
        self.createTree(root, res, total)
        return root

    def createTree(self, root, res, total):
        if root is not None:
            self.createTree(root.left, res, total)
            root.val = total - res[0]
            res.pop(0)
            self.createTree(root.right, res, total)

    def treeSum(self, root, res):
        if root is not None:
            self.treeSum(root.left, res)
            res.append(res[-1] + root.val)
            self.treeSum(root.right, res)
