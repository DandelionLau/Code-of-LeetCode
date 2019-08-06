class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.scan(root, res)
        return res
        
    def scan(self, root, res):
        if root is not None:
            self.scan(root.left, res)
            res.append(root.val)
            self.scan(root.right, res)
            
