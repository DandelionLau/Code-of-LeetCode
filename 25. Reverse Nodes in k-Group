class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # add a head node
        pre = ListNode(0)
        pre.next = head
        length = 0
        if k == 0 or k == 1:
            return head
        temp = pre
        while temp is not None and temp.next is not None:
            temp = self.reverse(temp, k)
        return pre.next

    def reverse(self, pre, k):
        prelist = [pre]
        first = pre.next
        second = first
        temp = k
        while temp > 1:
            prelist.append(second)
            if second.next == None:  # the last group is shorter than k
                return
            else:
                second = second.next
            temp = temp - 1
        prelist.append(second)
        x = second.next
        # start reversing from behind to front
        i = k
        while i > 0:
            prelist[i].next = prelist[i - 1]
            i = i - 1

        pre.next = second
        first.next = x
        return first  # the previou node of the next group
