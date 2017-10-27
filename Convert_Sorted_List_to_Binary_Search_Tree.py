x2# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# First converted into Array List, then convert it as the same as 'Convert_Sorted_Array_to_Binary_Search_Tree'.
# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 255 ms
# Your runtime beats 64.85 % of python submissions.
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        nums = []
        while head:
            nums += head.val,
            head = head.next

        def convert(nums):
            if nums:
                if len(nums) == 1:
                    return TreeNode(nums[0])
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = convert(nums[:mid])
                root.right = convert(nums[mid + 1:])
                return root

        return convert(nums)


# Use the slow and fast nodes to cut the linked list half, the slow node is the root of subtree.
# And delete the pre-slow node to avoid handle the same node in next iterate.
# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 249 ms
# Your runtime beats 74.20 % of python submissions.
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def convert(head):
            if not head:
                return None
            if head.next is None:
                return TreeNode(head.val)
            slow = fast = head
            while fast and fast.next:
                pre = slow  # Avoid to handle the same val in next iterate.So it is necessary to delete the slow node.
                slow = slow.next
                fast = fast.next.next
            pre.next = None # Avoid to handle the same val in next iterate.So it is necessary to delete the slow node.
            root = TreeNode(slow.val)
            root.left = convert(head)
            root.right = convert(slow.next)

            return root

        return convert(head)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().sortedListToBST(head))
