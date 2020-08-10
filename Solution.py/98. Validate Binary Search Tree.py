class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodes = []
        self.scan(root, nodes)
        
        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i-1]:
                return False
        return True
    
    
    
    def scan(self, root, nodes):
        if root is not None:
            self.scan(root.left, nodes)
            nodes.append(root.val)
            self.scan(root.right, nodes)
