# -*- encoding:utf-8 -*-
# __author__=='Gan'
#

# Given a binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any
# node in the tree along the parent-child connections. The path must contain at least one node
# and does not need to go through the root.
# For example:
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return 6.
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 92 / 92 test cases passed.
# Status: Accepted
# Runtime: 148 ms
# Your runtime beats 67.97 % of python submissions.
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_path_down(root):
            if not root:
                return 0
            left = max(0, max_path_down(root.left))  # Handle the negative
            right = max(0, max_path_down(root.right))
            self.max_value = max(self.max_value, left + right + root.val)
            return max(left, right) + root.val

        self.max_value = float('-inf')
        max_path_down(root)
        return self.max_value


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(10)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    print(Solution().maxPathSum(root))
