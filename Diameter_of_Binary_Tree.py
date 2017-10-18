# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def diameter(node):
            if not node:
                return 0
            node_left = diameter(node.left)
            node_right = diameter(node.right)
            self.max_diameter = max(self.max_diameter, node_left + node_right)
            return max(node_left, node_right) + 1
        self.max_diameter = 0
        diameter(root)
        return self.max_diameter


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.right = TreeNode(2)
    print(Solution().diameterOfBinaryTree(root))


# 106 / 106 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Your runtime beats 82.08 % of python submissions.
