# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        node_stack = [root]
        ans = []

        while node_stack:
            temp_stack = []
            sum_ = 0
            for node in node_stack:
                sum_ += node.val
                if node.left:
                    temp_stack += node.left,
                if node.right:
                    temp_stack += node.right,
            ans += sum_ / len(node_stack),
            node_stack = temp_stack
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(2)
    print(Solution().averageOfLevels(root))

