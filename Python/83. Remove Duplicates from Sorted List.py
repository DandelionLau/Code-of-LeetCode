"""
@FileName: 83. Remove Duplicates from Sorted List.py
@Description: Implement 83. Remove Duplicates from Sorted List
@Author: Ryuk
@CreateDate: 2021/06/27
@LastEditTime: 2021/06/27
@LastEditors: Please set LastEditors
@Version: v0.1
"""

from utils.linklist import *

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        while tmp is not None:
            if tmp.next is not None and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head


if __name__ == "__main__":
    data = [1,2,2,3,3,4]
    head = creat_linklist(data)
    print_linklist(head)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    print_linklist(result)