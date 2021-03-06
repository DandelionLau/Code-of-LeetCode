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
            
            
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
'''
