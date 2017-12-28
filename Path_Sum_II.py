# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 114 / 114 test cases passed.
# Status: Accepted
# Runtime: 106 ms
# Your runtime beats 5.29 % of python submissions.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(root, cur_sum, path):
            if not root:
                return
            cur_sum += root.val
            path += root.val,
            if not root.left and not root.right and cur_sum == sum:
                paths.append(path)
            dfs(root.left, cur_sum, list(path))
            dfs(root.right, cur_sum, list(path))

        paths = []
        dfs(root, 0, list())
        return paths


# 114 / 114 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 11.31 % of python submissions.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans, temp = list(), list()

        def dfs(root, val):
            if root:
                temp.append(root.val)
                if not root.left and not root.right and val == root.val:
                    ans.append(list(temp))
                else:
                    dfs(root.left, val - root.val)
                    dfs(root.right, val - root.val)
                temp.pop()

        dfs(root, sum)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().pathSum(root, 3))
    print(Solution().pathSum(TreeNode(1), 1))
