# -*- encoding:utf-8 -*-
# __author__=='Gan'


# The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called the "root." Besides the root,
#  each house has one and only one parent house. After a tour,
# the smart thief realized that "all houses in this place forms a binary tree".
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#      3
#     / \
#    2   3
#     \   \
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 124 / 124 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Your runtime beats 69.34 % of python submissions.
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs_rob(root):
            if not root:
                return (0, 0)
            l = dfs_rob(root.left)
            r = dfs_rob(root.right)
            return l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val)

        return dfs_rob(root)[1]


if __name__ == '__main__':
    head = TreeNode(10)
    head.left = TreeNode(4)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(3)
    head.right = TreeNode(5)
    head.right.left = TreeNode(1)
    print(Solution().rob(head))



    # print(Solution().rob(None))
