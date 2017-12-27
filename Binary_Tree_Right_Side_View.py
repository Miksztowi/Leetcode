# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
# ordered from top to bottom.
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#
# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 210 / 210 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 69.98 % of python submissions.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            ans.append(stack[-1].val)
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]
        return ans


# 210 / 210 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 38.90 % of python submissions.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]


# 210 / 210 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 24.66 % of python submissions.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)

                collect(node.right, depth + 1)
                collect(node.left, depth + 1)
        view = []
        collect(root, 0)
        return view





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().rightSideView(root))
    print(Solution().rightSideView((None)))
