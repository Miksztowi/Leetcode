# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 55 ms
# Your runtime beats 24.73 % of python submissions.
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        order_path = [[root.val]]
        front = rear = depth = 0
        node_stack = [[root]]
        dummy_stack = []
        while front <= rear:
            if node_stack[depth][front]:
                if node_stack[depth][front].left:
                    rear += 1
                    dummy_stack.append(node_stack[depth][front].left)
                if node_stack[depth][front].right:
                    rear += 1
                    dummy_stack.append(node_stack[depth][front].right)
            if len(node_stack[depth]) - 1 == front:
                depth += 1
                node_stack.append(dummy_stack)
                rear = len(dummy_stack) - 1
                if dummy_stack:
                    dummy_path = []
                    for node in dummy_stack:
                        dummy_path += node.val,
                    order_path += dummy_path,
                    dummy_stack = []
                front = 0
            else:
                front += 1

        return order_path


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Your runtime beats 58.77 % of python submissions.
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        order_paths = []
        while level:
            temp = []
            order_paths += [],
            for node in level:
                order_paths[-1] += node.val,
                if node.left:
                    temp += node.left,
                if node.right:
                    temp += node.right,
            level = temp

        return order_paths


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))