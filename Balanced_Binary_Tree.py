# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ by more than 1.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 79 ms
# Your runtime beats 52.96 % of python submissions.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def subtrees_depth(root):
            if not root:
                return 0
            root.left_depth = subtrees_depth(root.left) + 1
            root.right_depth = subtrees_depth(root.right) + 1
            return max(root.left_depth, root.right_depth)

        subtrees_depth(root)

        def is_balanced(root):
            if not root:
                return True
            if abs(root.left_depth - root.right_depth) > 1:
                return False
            return is_balanced(root.left) and is_balanced(root.right)

        return is_balanced(root)


# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 88.83 % of python submissions.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs_height(root):
            if not root:
                return 0
            left_height = dfs_height(root.left)
            if left_height == -1:
                return -1
            right_height = dfs_height(root.right)
            if right_height == -1:
                return -1

            return -1 if abs(left_height - right_height) > 1 else max(left_height, right_height) + 1

        return dfs_height(root) != -1


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    # result = Solution().isBalanced(root)
    # print(result)
    root.left.left = TreeNode(2)
    # root.left.left.left = TreeNode(2)
    # root.left.left.left.left = TreeNode(2)
    result = Solution().isBalanced(root)
    print(result)
