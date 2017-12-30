# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, find the length of the longest path where each node in the path has the same value.
# This path may or may not pass through the root.
# Note: The length of path between two nodes is represented by the number of edges between them.
# Example 1:
# Input:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2
# Example 2:
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 879 ms
# Your runtime beats 15.67 % of python submissions.
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(root):
            if root:
                left_len, right_len = traverse(root.left), traverse(root.right)
                left_len = (left_len + 1) if root.left and root.val == root.left.val else 0
                right_len = (right_len + 1) if root.right and root.val == root.right.val else 0
                self.ans = max(self.ans, left_len + right_len)
                return max(left_len, right_len)
            return 0

        self.ans = 0
        traverse(root)
        return self.ans


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 679 ms
# Your runtime beats 80.47 % of python submissions.
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        length_list = []
        def getlongest(root, pre_val):
            if root:
                if root.val == pre_val:
                    return 1 + max(getlongest(root.left, root.val), getlongest(root.right, root.val))
                else:
                    length_list.append((getlongest(root.left, root.val) + getlongest(root.right, root.val)))
                    return 0
            return 0
        getlongest(root, None)
        return max(length_list) if length_list else 0
    
if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().longestUnivaluePath(root))
