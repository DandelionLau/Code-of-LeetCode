# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        listA = []
        listB = []
        
        while headA is not None:
            listA.append(headA)
            headA = headA.next
        
        while headB is not None:
            listB.append(headB)
            headB = headB.next
        
        if listA[-1] != listB[-1]:
            return None
        
        pre = listA[-1]
        while len(listA) > 0 and len(listB) > 0:
            a = listA.pop()
            b = listB.pop()
            if a != b:
                return pre
            pre = a
            
        return pre
