"""
@FileName: 100. Same Tree.py
@Description: Implement 100. Same Tree
@Author: Ryuk
@CreateDate: 2021/06/20
@LastEditTime: 2021/06/20
@LastEditors: Please set LastEditors
@Version: v0.1
"""
from utils import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    p = [1, 2, 3]
    q = [1, None, 3]
    p = generate_tree(p, 0)
    q = generate_tree(q, 0)

    sol = Solution()
    result = sol.isSameTree(p, q)
    print(result)

if __name__ == '__main__':
    main()