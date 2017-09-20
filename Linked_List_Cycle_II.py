# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Note: Do not modify the linked list.
# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        hare = tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                break

        if not (hare and hare.next):
            return None

        tortoise = head
        while hare != tortoise:
            tortoise = tortoise.next
            hare = hare.next
        return hare


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = head.next
    print(Solution().detectCycle(head))

# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 96 ms
# Your runtime beats 16.96 % of python submissions.

# https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
# Here is algorithm about cycle detection