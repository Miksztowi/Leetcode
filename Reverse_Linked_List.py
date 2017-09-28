# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Reverse a singly linked list.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

# Recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(head, prev=None):
            if not head:
                return prev
            node = head.next
            head.next = prev
            return reverse(node, head)

        return reverse(head)

if __name__ == '__main__':
    head = ListNode(0)
    A = ListNode(1)
    B = ListNode(2)
    head.next = A
    A.next = B
    print(head, A, B)
    reverse = Solution().reverseList(head)
    while reverse:
        print(reverse)
        reverse = reverse.next


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 75.29 % of python submissions.

