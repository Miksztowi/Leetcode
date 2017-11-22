# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# From pre ---> a ---> b ---> b.next to pre ---> b ---> a ---> b.next. Then pre = a.
# 55 / 55 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 40.30 % of python submissions.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # it equals to pre, pre.next = self, head.
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        self.printf(dummy.next)
        return dummy.next

    def printf(self, head):
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    result = Solution().swapPairs(head)
    print(result)
