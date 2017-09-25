# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummy_a = headA
        dummy_b = headB
        len_a, len_b = 0, 0
        while dummy_a:
            len_a += 1
            dummy_a = dummy_a.next
        while dummy_b:
            len_b += 1
            dummy_b = dummy_b.next

        set_a, set_b = headA, headB

        if len_a > len_b:
            while len_a > len_b:
                len_a -= 1
                set_a = set_a.next
        else:
            while len_b > len_a:
                len_b -= 1
                set_b = set_b.next

        while set_a and set_b:
            if set_a == set_b:
                return set_a
            set_a = set_a.next
            set_b = set_b.next


if __name__ == '__main__':
    head_a = ListNode(0)
    head_b = ListNode(0)
    head_a.next = ListNode(1)
    head_b.next = ListNode(1)
    a = ListNode(2)
    head_a.next.next = head_b.next.next = a
    print(Solution().getIntersectionNode(head_a, head_b))


# 42 / 42 test cases passed.
# Status: Accepted
# Runtime: 375 ms
# Your runtime beats 85.35 % of python submissions.


# Here is the fastest solution from Leetcode.
# len_a = 5, len_b = 6. Make a = 5+6 and b = 6+5. Then they are the same length.
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
