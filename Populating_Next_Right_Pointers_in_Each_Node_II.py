# -*- encoding:utf-8 -*-
# __author__=='Gan'



# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution still work?
# Note:
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# BFS, use dummy pointer to point the head of next level.
# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 51.02 % of python submissions.
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = tail = TreeLinkNode(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next


if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.right = TreeLinkNode(2)
    print(Solution().connect(root))
