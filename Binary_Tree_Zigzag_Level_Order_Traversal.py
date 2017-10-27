# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
# then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 35.54 % of python submissions.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_stack = [root]
        order_path = []
        level = 0
        while node_stack:
            level += 1
            temp_stack = []
            order_path += [],
            for node in node_stack:
                if level % 2:
                    order_path[-1] += node.val,
                else:
                    order_path[-1].insert(0, node.val)
                if node.left:
                    temp_stack += node.left,
                if node.right:
                    temp_stack += node.right,
            node_stack = temp_stack
        return order_path


# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 35.54 % of python submissions.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def bfs_level(root, level):
            if len(self.ans) < level + 1:
                self.ans += [root.val],
            elif not level % 2:
                self.ans[level] += root.val,
            else:
                self.ans[level].insert(0, root.val)
            if root.left:
                bfs_level(root.left, level+1)
            if root.right:
                bfs_level(root.right, level+1)

        self.ans = []
        bfs_level(root, 0)
        return self.ans


# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 38 ms
# Your runtime beats 83.13 % of python submissions.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_stack = [root]
        order_path = []
        level = 0
        while node_stack:
            temp_path = [x.val for x in node_stack]
            level += 1
            if level % 2:
                order_path += temp_path,
            else:
                order_path += temp_path[::-1],

            node_stack = [child for x in node_stack for child in (x.left, x.right) if child]

        return order_path


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().zigzagLevelOrder(root))
