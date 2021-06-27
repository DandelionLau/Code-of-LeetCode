"""
@FileName: tree.py
@Description: Implement tree
@Author: Ryuk
@CreateDate: 2021/06/27
@LastEditTime: 2021/06/27
@LastEditors: Please set LastEditors
@Version: v0.1
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(data: List[int], index:int)->TreeNode:
    if index < len(data):
        if data[index] is None:
            return None
        else:
            root = TreeNode(data[index])
            root.left = create_tree(data, 2*index+1)
            root.right = create_tree(data, 2*index+2)
        return root
    else:
        return None

def print_tree(root:TreeNode, height:int, label:str, length:int):
    if root is None:
        return

    print_tree(root.right, height+1, "/ ", length)
    val = label + str(root.val)
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM - lenL
    val = " " * lenL + val + " " * lenR
    print(height * "      ",val)
    print_tree(root.left, height + 1, "\\ ", length)


if __name__ == '__main__':
    data = [1,2,3,4,5]
    root = generate_tree(data, 0)
    print_tree(root, 0, " ", 10)