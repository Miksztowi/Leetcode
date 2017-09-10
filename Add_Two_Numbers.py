# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            res = carry
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            carry, res = res // 10, res % 10  # 3.x  5/2 = 2.5, so if want to get 2.Use '//'

            current.next = ListNode(res)
            current = current.next

            if carry == 1:
                current.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    res = Solution().addTwoNumbers(a,b)
    while res:
        print(res.val)
        res = res.next

# 1562 / 1562 test cases passed.
# Status: Accepted
# Runtime: 122 ms
# Your runtime beats 65.56 % of python submissions
