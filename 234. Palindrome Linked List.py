# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        p = head
        while p is not None:
            stack.append(p.val)
            p = p.next
        
        i = 0
        j = len(stack) - 1
        while i <= j:
            if stack[i] == stack[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
