# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 193 / 193 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 31.22 % of python submissions.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(left, right):
            if not (left or right):
            # if left is None and right is None:
                return True
            if not left or not right:
                return False

            if left.val == right.val:
                out_pair = is_mirror(left.left, right.right)
                in_pair = is_mirror(left.right, right.left)
                return out_pair and in_pair
            else:
                return False

        if not root:
            return True
        else:
            return is_mirror(root.left, root.right)


# 193 / 193 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 40.54 % of python submissions.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        node_list = [[root.left, root.right]]
        while node_list:
            left_node, right_node = node_list.pop()
            if left_node is right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            node_list.append([left_node.left,right_node.right])
            node_list.append([left_node.right,right_node.left])

        return True




if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.right = TreeNode(1)
    print(Solution().isSymmetric(root))