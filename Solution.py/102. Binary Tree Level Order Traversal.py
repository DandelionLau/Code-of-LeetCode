class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        tmp = []
        queue = [root]
        count = 1
        next_count = len(queue)

        while len(queue) > 0:
            node = queue.pop(0)
            tmp.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

            if count == next_count:
                res.append(tmp)
                tmp = []
                count = 0
                next_count = len(queue)
            count += 1
        return res
