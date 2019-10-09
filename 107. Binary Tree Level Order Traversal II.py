class Solution(object):
    def levelOrderBottom(self, root):
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
                res.append(tmp)
                tmp = []
        res.reverse()
        return res
