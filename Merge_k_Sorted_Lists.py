# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution: Use Priority Queue.
# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 245 ms
# Your runtime beats 18.57 % of python submissions.
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        root = current_node = ListNode(0)
        priority = PriorityQueue()
        for node in lists:
            if node:
                priority.put((node.val, node))

        while priority.qsize() > 0:
            current_node.next = priority.get()[1]
            current_node = current_node.next
            if current_node.next:
                priority.put((current_node.next.val, current_node.next))

        return root.next


# Solution: Iterative to get all node, and sort them by value. Then the next of node_list[i] is node_list[i+1].
# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 97.44 % of python submissions.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_lists = []
        for node in lists:
            current_node = node  # Protect the Original data.
            while current_node:
                node_lists.append(current_node)
                current_node = current_node.next

        node_lists.sort(key=lambda x: x.val)

        for i in range(len(node_lists) - 1):
            node_lists[i].next = node_lists[i+1]

        if node_lists:
            return node_lists[0]
        else:
            return None


# Time Limit Exceeded
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if not lists:
#             return None
#
#         root = current_node = ListNode(0)
#         current_min_index = 0
#
#         while any(lists):
#             for i in range(len(lists)):
#                 if lists[i]:
#                     current_min_index = i
#             for i in range(len(lists)):
#                 if lists[i]:
#                     if lists[i].val < lists[current_min_index].val:
#                         current_min_index = i
#             current_node.next = lists[current_min_index]
#             current_node = current_node.next
#             lists[current_min_index] = lists[current_min_index].next
#
#         return root.next

if __name__ == '__main__':
    print(Solution().mergeKLists([ListNode(2), ListNode(1)]))


