# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# Your runtime beats 14.06 % of python submissions.
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_stack = [root]
        order_path = []
        while node_stack:
            temp = []
            order_path.insert(0, [])
            for node in node_stack:
                order_path[0] += node.val,
                if node.left:
                    temp += node.left,
                if node.right:
                    temp += node.right,
            node_stack = temp

        return order_path


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Your runtime beats 63.54 % of python submissions.
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def bfs_traversal(root, order_path, index):
            if not root:
                return None

            if len(order_path) < index + 1:  # make the left and right sides at the same level.
                order_path += [root.val],
            else:
                order_path[index] += root.val,

            bfs_traversal(root.left, order_path, index+1)
            bfs_traversal(root.right, order_path, index+1)

        order_path = []
        bfs_traversal(root, order_path, 0)

        return order_path[::-1]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(root))


