# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        hare, tortoise = head, head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False

    def hasCycle(self, head):
        if not head:
            return False
        power = lam = 1
        tortoise = head
        hare = head.next  # f(x0) is the element/node next to x0.
        while hare and hare.next:
            if power == lam:  # time to start a new power of two?
                tortoise = hare
                power *= 2
                lam = 0
            hare = hare.next
            lam += 1
            if tortoise == hare:
                return True
        return False


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(10)
    # head.next.next = head
    print(Solution().hasCycle(head))


# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 75 ms
# Your runtime beats 58.67 % of python submissions.

# https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
# Here is algorithm about cycle detection
