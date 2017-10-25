# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, return the inorder traversal of its nodes' values.
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def in_order(root):
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []

        return in_order(root)


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 10.55 % of python submissions.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_stack = [root]
        order_path = []
        while node_stack:
            node = node_stack[-1]
            if node.left == 1:
                order_path.append(node.val)
                node.left = 0
            elif node.left:
                node_stack.append(node.left)
                node.left = 1
            elif node.left is None:
                node.left = 1
            elif node.right:
                node_stack.append(node.right)
                node.right = None
            else:
                node = node_stack.pop()

        return order_path


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 44.49 % of python submissions.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_stack = []
        order_path = []
        p = root
        while node_stack or p:
            if p:
                node_stack += p,
                p = p.left
            else:
                node = node_stack.pop()
                order_path += node.val,
                p = node.right

        return order_path


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(2)
    result = Solution().inorderTraversal(root)
    print(result)
