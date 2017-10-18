# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
# is changed to the original key plus sum of all keys greater than the original key in BST.
# Example:
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 212 / 212 test cases passed.
# Status: Accepted
# Runtime: 115 ms
# Your runtime beats 63.18 % of python submissions.
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.added_nums = 0
        def traverse_add(node):
            if node:
                traverse_add(node.right)
                node.val += self.added_nums
                self.added_nums = node.val
                traverse_add(node.left)

        traverse_add(root)
        return root


# 212 / 212 test cases passed.
# Status: Accepted
# Runtime: 155 ms
# Your runtime beats 14.20 % of python submissions.
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse(node):
            return reverse(node.right) + [node] + reverse(node.left) if node else []
        for a, b in zip(reverse(root), reverse(root)[1:]):
            b.val += a.val
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(1)
    root.right = TreeNode(13)
    print(Solution().convertBST(root))





