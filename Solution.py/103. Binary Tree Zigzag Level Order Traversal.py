class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        queue = [root]
        count = 0
        next_count = 1
        flag = 0
        res = []
        tmp = []
        while len(queue) > 0:
            node = queue.pop(0)
            tmp.append(node.val)
            count += 1

            if node.left is not None:
                if node.left.val is not None:
                    queue.append(node.left)
            if node.right is not None:
                if node.right.val is not None:
                    queue.append(node.right)

            if count == next_count:
                count = 0
                next_count = len(queue)
                if flag == 0:
                    res.append(tmp)
                    flag = 1
                else:
                    tmp.reverse()
                    res.append(tmp)
                    flag = 0
                tmp = []

        return res
