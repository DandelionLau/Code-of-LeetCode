class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next

        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        index = len(nums) // 2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        return root
