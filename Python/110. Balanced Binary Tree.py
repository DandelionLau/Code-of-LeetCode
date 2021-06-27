"""
@FileName: 110. Balanced Binary Tree.py
@Description: Implement 110. Balanced Binary Tree
@Author: Ryuk
@CreateDate: 2021/06/27
@LastEditTime: 2021/06/27
@LastEditors: Please set LastEditors
@Version: v0.1
"""
from utils.tree import *

class Solution:
    def height(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is not None:
            if abs(self.height(root.left) - self.height(root.right)) > 1:
                return False

            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True

if __name__ == "__main__":
    data = [1,2,2,3,3,None,None,4,4]
    root = create_tree(data, 0)
    print_tree(root, 0, " ", 10)
    solution = Solution()
    result = solution.isBalanced(root)
    print(result)
