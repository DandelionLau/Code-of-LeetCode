
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        head_node = ListNode(None)
        head_node.next = head

        tail = head
        length = 1
        while tail.next is not None:
            length += 1
            tail = tail.next

        if length == 1:
            return head_node.next

        k = k % length

        # 移动 length - k 个结点
        for i in range(abs(k-length)):
            tmp = head_node.next
            head_node.next = tmp.next
            tmp.next = None
            tail.next = tmp
            tail = tmp

        return head_node.next
