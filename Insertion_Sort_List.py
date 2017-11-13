# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):  # None or one node, don't sort.
            return head
        sorted_node = head
        while sorted_node.next and sorted_node.next.val > sorted_node.val:  # If Linked List have been sorted,don't sort
            sorted_node = sorted_node.next
        if not sorted_node.next:
            return head

        helper = ListNode(0)  # helper.next will be the head.
        cur = head  # the current node needs to be sorted.
        pre = helper  # the current node will insert between pre and pre.next.
        while cur:
            next_ = cur.next  # next sort node.
            while pre.next and pre.next.val <= cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = next_
        return helper.next

    def print_list(self, head):
        head = self.insertionSortList(head)
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)
    print(Solution().print_list(head))
