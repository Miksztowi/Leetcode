# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        counter, incise = dummy, dummy
        for i in range(n):
            counter = counter.next  # if len = 10 and n = 5, from 0 to 5 and from 10 to 5 are the same.
        while counter.next:
            counter, incise = counter.next, incise.next
            # Find the location where need to incise.
        incise.next = incise.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().removeNthFromEnd(head, 1))



# 207 / 207 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 46.63 % of python submissions.

# Summary:
# If only traverse the list,then there are several operations.
# Then it should be linked to the list several times.
# For this question, find the location and incise the list are two operations.So it should be linked to the list twice.

