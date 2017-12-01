# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 1563 / 1563 test cases passed.
# Status: Accepted
# Runtime: 132 ms
# Your runtime beats 54.33 % of python submissions.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(None)
        current = dummy
        list_1, list_2 = [], []
        while l1:
            list_1 += l1.val,
            l1 = l1.next
        while l2:
            list_2 += l2.val,
            l2 = l2.next

        val_list = []
        while list_1 or list_2:
            res = carry
            if list_1:
                res += list_1.pop()
            if list_2:
                res += list_2.pop()
            res, carry = res % 10, res // 10
            val_list.insert(0, res)

        if carry:
            val_list.insert(0, carry)

        for val in val_list:
            current.next = ListNode(val)
            current = current.next

        return dummy.next


# 1563 / 1563 test cases passed.
# Status: Accepted
# Runtime: 142 ms
# Your runtime beats 37.62 % of python submissions.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = n2 = n = 0
        pre = None
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
        n += n1 + n2
        if n == 0:
            return ListNode(0)
        while n:
            cur = ListNode(n % 10)  # Note here.
            cur.next = pre
            pre = cur
            n = n // 10

        return pre


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    res = Solution().addTwoNumbers(a, b)
    while res:
        print(res.val)
        res = res.next
