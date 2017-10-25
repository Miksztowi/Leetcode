# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, return the postorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
# Note: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 67 / 67 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 45.96 % of python submissions.
class Solution(object):
    def postorderTraversal(self, root):
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
            if node.left:
                node_stack.append(node.left)
                node.left = None
            elif node.right:
                node_stack.append(node.right)
                node.right = None
            else:
                node = node_stack.pop()
                order_path.append(node.val)

        return order_path


# 67 / 67 test cases passed.
# Status: Accepted
# Runtime: 29 ms
# Your runtime beats 94.03 % of python submissions.
class Solution(object):
    def postorderTraversal(self, root):
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
                order_path.insert(0, p.val)
                p = p.right
            else:
                node = node_stack.pop()
                p = node.left

        return order_path


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(2)
    result = Solution().postorderTraversal(root)
    print(result)
