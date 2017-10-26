# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so fuck off.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 43.80 % of python submissions.
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(root.left)
        # above is wrong
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(2)
    result = Solution().invertTree(root)
    print(result)
