# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 9 / 9 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 31.68 % of python submissions.
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_tree(node, left, right):
            node = TreeNode(node)
            node.left = left
            node.right = right
            return node

        def trees(start, end):
            return [generate_tree(node, left, right)
                    for node in range(start, end)
                    for left in trees(start, node)
                    for right in trees(node + 1, end)] or [None]

        return trees(1, n + 1)

    def pre_order(self, root):
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right) if root else []


if __name__ == '__main__':
    ans = Solution().generateTrees(3)
    for i in ans:
        print(Solution().pre_order(i))
