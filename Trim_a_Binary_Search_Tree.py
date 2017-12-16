# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree,
# so the result should return the new root of the trimmed binary search tree.
#
# Example 1:
# Input:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output:
#     1
#       \
#        2
# Example 2:
# Input:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output:
#       3
#      /
#    2
#   /
#  1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 77 / 77 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Your runtime beats 63.60 % of python submissions.
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if L > root.val:
                return dfs(root.right)
            if R < root.val:
                return dfs(root.left)
            return root

        return dfs(root)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right = TreeNode(4)
    result = Solution().trimBST(root, 1, 3)


    def printf(root):
        return [root.val] + printf(root.left) + printf(root.right) if root else []


    print(printf(result))
