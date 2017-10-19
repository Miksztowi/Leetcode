# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root, cur_depth):
            if not root:
                return 0
            root.depth = cur_depth
            self.max_depth = max(self.max_depth, root.depth)
            max_depth(root.left, cur_depth + 1)
            max_depth(root.right, cur_depth + 1)

        self.max_depth = 0
        max_depth(root, 1)

        return self.max_depth


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, [root.left, root.right])) if root else 0


# Much Fun!
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return root and 1 + max(map(self.maxDepth, [root.left, root.right])) or 0



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.right = TreeNode(1)
    print(Solution().maxDepth(root))
