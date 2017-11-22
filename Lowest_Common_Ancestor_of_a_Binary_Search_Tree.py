# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that
#  has both v and w as descendants (where we allow a node to be a descendant of itself).”
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example
# is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Both p and q smaller node, the answer will in left subtree.
# Both p and q greater than node, the answer will in right subtree.
# Otherwise the node is answer.
# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 115 ms
# Your runtime beats 75.21 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.val > root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 116 ms
# Your runtime beats 71.68 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if q.val > root.val < p.val:
                root = root.right
            elif q.val < root.val > p.val:
                root = root.left
            else:
                return root


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 152 ms
# Your runtime beats 11.25 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.left.right = TreeNode(4)
    root.right = TreeNode(8)
    result = Solution().lowestCommonAncestor(root, root.left, root.right)
    print(result.val)
