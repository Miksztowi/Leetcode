# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 392 ms
# Your runtime beats 50.66 % of python submissions.
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge_list(l1, l2)

    def merge_list(self, l1, l2):
        l = ListNode(None)
        p = l
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2
        return l.next

    def print_list(self, head):
        head = self.sortList(head)
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)
    print(Solution().sortList(head))
