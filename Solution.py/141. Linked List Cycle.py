class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        p = head.next
        q = head.next.next

        while p.next is not None and q is not None:
            if q.next == p:
                return True
            else:
                try:
                    p = p.next
                    q = q.next.next
                except:
                    break
        return False
