class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return 
        
        root = TreeNode(None)
        self.tree(preorder, inorder, root)
        return root


    def tree(self, preorder, inorder, root):
        if len(preorder) > 0:
            root.val = preorder[0]
            if len(preorder) == 1:
                return root
            # 找到根节点在中序遍历序列中的位置
            root_index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1+root_index], inorder[0:root_index])
            root.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])
