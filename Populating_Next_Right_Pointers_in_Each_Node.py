# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Note:
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level,
# and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# You may only use constant extra space.!!!!!!
# 14 / 14 test cases passed.
# Status: Accepted
# Runtime: 85 ms
# Your runtime beats 38.83 % of python submissions.
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        stack = [root]
        nodes_level = []
        while stack:
            next_level = []
            for node in stack:
                if node.left:
                    next_level += node.left,
                if node.right:
                    next_level += node.right,
            stack = next_level
            nodes_level.append(next_level)

        for level in nodes_level:
            for i in range(len(level)):
                if i != len(level) - 1:
                    level[i].next = level[i + 1]


# 14 / 14 test cases passed.
# Status: Accepted
# Runtime: 79 ms
# Your runtime beats 60.70 % of python submissions.
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            next_ = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next_


if __name__ == '__main__':
    root = TreeLinkNode(1)
    print(Solution().connect(root))
