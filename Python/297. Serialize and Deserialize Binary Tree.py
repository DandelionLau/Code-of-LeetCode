class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None or node.val is None:
                res.append("null")
            else:
                res.append(str(node.val))

            if node is not None:
                queue.append(node.left)
                queue.append(node.right)

        # cut
        i = len(res)-1
        while i > 0:
            if res[-1] != "null":
                break
            try:
                if res[i] == "null" and res[i-1] == "null":
                    res.pop()
            except:
                break
            i -= 1

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return
        return self.create(data, 0)

    def create(self, data, i):
        if i >= len(data):
            return
        root = TreeNode(data[i])
        root.left = self.create(data, 2 * i + 1)
        root.right = self.create(data, 2 * i + 2)
        return root
