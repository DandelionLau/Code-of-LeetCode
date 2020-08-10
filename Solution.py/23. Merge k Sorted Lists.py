# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = []
        if len(lists) == 0:
            return
        elif len(lists) == 1:
            return lists[0]
        # merge two lists
        elif len(lists) == 2:
            # the sorted list
            p = lists[0]
            q = lists[1]

            new = ListNode(0)
            # sort the first elements
            # if list is empty
            if p == None:
                return q
            elif q == None:
                return p
            elif q == None and q == None:
                return 
            # no empty list
            elif p.val > q.val:
                new = q
                q = q.next
            else:
                new = p
                p = p.next
                
            temp = new
            
            while p != None and q != None:
                if p.val > q.val:
                    temp.next = q
                    q = q.next
                else:
                    temp.next = p
                    p = p.next
                temp = temp.next
            
            if p != None:
                temp.next = p
            else:
                temp.next = q
                
            return new
        else:
            i = 0
            j = len(lists) - 1
            while i < j:
                temp = [lists[i],lists[j]]
                result.append(self.mergeKLists(temp))
                i = i + 1
                j = j - 1
            if i == j:
                result.append(lists[i])
                
        return self.mergeKLists(result)
                
                
