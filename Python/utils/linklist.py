"""
@FileName: linklist.py
@Description: Implement linklist
@Author: Ryuk
@CreateDate: 2021/06/27
@LastEditTime: 2021/06/27
@LastEditors: Please set LastEditors
@Version: v0.1
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def creat_linklist(data):
    if len(data) == 0:
        return None
    head = ListNode(data[0])
    tmp = head
    for i in range(1, len(data)):
        tmp.next = ListNode(data[i])
        tmp = tmp.next
    return head


def print_linklist(head):
    while head is not None:
        print(head.val,end="->")
        head = head.next
    print()



if __name__ == '__main__':
    data = [1,2,3,4,5]
    head = creat_linklist(data)
    print_linklist(head)
