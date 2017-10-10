# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Reversed first half == second half
# phase 1: Reverse the first half while finding middle.
# phase 2: Compare the reversed first half with the second half.
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = tortoise = head
        rev = None  # The last node is None.
        while hare and hare.next:
            hare = hare.next.next
            rev, rev.next, tortoise = tortoise, rev, tortoise.next
        tortoise = tortoise.next if hare else tortoise
        while tortoise and tortoise.val == rev.val:
            tortoise = tortoise.next
            rev = rev.next
        return not tortoise


# Solution 1: Reversed first half == second half
# phase 1: Reverse the first half while finding middle.
# phase 2: While comparing the two halves, restore the list to its original state by reversing the first back.
# !! play nice!!!!!
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = head
        rev = None  # The last node is None.
        while hare and hare.next:
            hare = hare.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if hare else head
        while rev and tail.val == rev.val:
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return not rev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))


# 26 / 26 test cases passed.
# Status: Accepted
# Runtime: 142 ms
# Your runtime beats 54.12 % of python submissions.

