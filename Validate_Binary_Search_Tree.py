# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Don't need to find the minimum number and maximum number.So this solution is too slow.
# 74 / 74 test cases passed.
# Status: Accepted
# Runtime: 122 ms
# Your runtime beats 3.61 % of python submissions.
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def find_min(root):
            return min(find_min(root.left), root.val) if root else float('inf')

        def find_max(root):
            return max(find_max(root.right), root.val) if root else float('-inf')

        min_ = find_min(root)
        max_ = find_max(root)

        def validate_tree(root, min_key, max_key):
            if not root:
                return True
            if root.val < min_key or root.val > max_key:
                return False
            return validate_tree(root.left, min_key, root.val-1) and validate_tree(root.right, root.val+1, max_key)

        return validate_tree(root, min_, max_)


# Validation rule: determine root.val <= min_key or roo.val >= max_key. if so, return false.
# Tips: >= or <= to handle the same number.
# 74 / 74 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 70.72 % of python submissions.
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def verify_validity(root, min_key, max_key):
            if not root:
                return True
            # >= or <= to handle the same number.
            if root.val <= min_key or root.val >= max_key:
                return False
            return verify_validity(root.left, min_key, root.val) and verify_validity(root.right, root.val, max_key)
        return verify_validity(root, float('-inf'), float('inf'))

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    # root.left = TreeNode(1)
    # root.left.left = TreeNode(2)
    # root.left.left.left = TreeNode(2)
    # root.left.left.left.left = TreeNode(2)
    print(Solution().isValidBST(root))
