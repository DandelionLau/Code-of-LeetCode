# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        head_node = ListNode(None)
        head_node.next = head
        
        pre_node = head_node
        cur_node = pre_node.next
        next_node = cur_node.next
        
        while cur_node.next is not None:
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            next_node = cur_node.next
        
        # handle the last node
        cur_node.next = pre_node
        
        head.next = None
        return cur_node
