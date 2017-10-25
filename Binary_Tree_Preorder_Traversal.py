# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 67 / 67 test cases passed.
# Status: Accepted
# Runtime: 29 ms
# Your runtime beats 94.69 % of python submissions.
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_stack = [root]
        order_path = [root.val]
        while node_stack:
            node = node_stack[-1]
            if node.left:
                order_path.append(node.left.val)
                node_stack.append(node.left)
                node.left = None
            elif node.right:
                order_path.append(node.right.val)
                node_stack.append(node.right)
                node.right = None
            else:
                node_stack.pop()

        return order_path


# 67 / 67 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 18.85 % of python submissions.
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p = root
        node_stack = []
        order_path = []
        while node_stack or p:
            if p:
                order_path += p.val,
                node_stack += p,
                p = p.left
            else:
                p = node_stack.pop()
                p = p.right

        return order_path


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(2)
    result = Solution().preorderTraversal(root)
    print(result)
