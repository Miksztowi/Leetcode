# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Remove all elements from a linked list of integers that have value val.
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 65 / 65 test cases passed.
# Status: Accepted
# Runtime: 102 ms
# Your runtime beats 76.41 % of python submissions.

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val != val:
                pre = head
            else:
                pre.next = head.next
            head = head.next
        self.printf(dummy.next)
        return dummy.next

    def printf(self, head):
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(10)
    head.next.next.next.next = ListNode(10)
    head.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next = ListNode(1)
    print(Solution().removeElements(head, 1))
