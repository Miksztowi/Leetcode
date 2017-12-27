# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all
# the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 114 / 114 test cases passed.
# Status: Accepted
# Runtime: 58 ms
# Your runtime beats 70.13 % of python submissions.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root, cur_sum):
            if not root:
                return False
            cur_sum += root.val
            if not root.left and not root.right and cur_sum == sum:
                return True
            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        return dfs(root, 0) if root else False



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().hasPathSum(root, 3))
    print(Solution().hasPathSum(TreeNode(1), 1))
