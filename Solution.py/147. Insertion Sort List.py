class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        nums = []
        tmp = head
        while tmp is not None:
            nums.append(tmp.val)
            tmp = tmp.next

        nums.sort()
        tmp = head
        i = 0
        while tmp is not None:
            tmp.val = nums[i]
            i += 1
            tmp = tmp.next
        return head
