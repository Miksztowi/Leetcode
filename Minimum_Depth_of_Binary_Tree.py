# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
# 41 / 41 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# Your runtime beats 56.61 % of python submissions.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs_depth(root):
            if not root:
                return 0
            left_depth = dfs_depth(root.left)
            right_depth = dfs_depth(root.right)
            if left_depth and right_depth:
                return min(left_depth, right_depth) + 1
            elif left_depth:
                return left_depth + 1
            elif right_depth:
                return right_depth + 1
            else:
                return 1
        return dfs_depth(root)


# BFS
# 41 / 41 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Your runtime beats 19.56 % of python submissions.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node_stack = [root]
        depth = 1
        while node_stack:
            temp = []
            for node in node_stack:
                if not (node.left or node.right):
                    return depth
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth += 1
            node_stack = temp


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().minDepth(root))

