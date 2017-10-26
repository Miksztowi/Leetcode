# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, flatten it to a linked list in-place.
# For example,
# Given
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 225 / 225 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 77.13 % of python submissions.
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def flatted(node):
            if node.left:
                temp = node.left
                while temp.right:
                    temp = temp.right
                temp.right, node.right = node.right, node.left
            node.left = None
            if node and node.right:
                flatted(node.right)

        flatted(root)

# Same as above.
# 225 / 225 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 77.13 % of python submissions.
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def flatted(node):
            if node.left:
                temp = node.left
                while temp.right:
                    temp = temp.right
                temp.right, node.right = node.right, node.left
            node.left = None

        def in_order(root):
            return in_order(root.left) + [root] + in_order(root.right) if root else []
        
        list(map(flatted, in_order(root)[::-1]))


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().flatten(root))
