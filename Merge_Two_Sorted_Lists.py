# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Frist, I use MECE to split the question.But i think it is too complex to split.So just use 'while' is better.
# But this questions still have other solutions need to think and practice,  even i got the anwser.
# Todo: More solutions.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (not l1) and l2:
            return l2
        if (not l2) and l1:
            return l1
        if not (l1 and l2):
            return None
        c = ListNode(0)
        dummy = c
        while l1 and l2:
            if l1.val < l2.val:  # Use 'and' not 'or',Because they are sorted lists.
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        c.next = l1 or l2
        return dummy.next

# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Your runtime beats 20.95 % of python submissions.



# Here are some solutions what i think very cool.
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


# in-place, iteratively
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode(2), ListNode(1)))



