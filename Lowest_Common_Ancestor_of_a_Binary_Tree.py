# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes v and w as the lowest node in T
# that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 146 ms
# Your runtime beats 18.30 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def pre_order(root, search_node, path, dummy):
            dummy += [root]
            if root == search_node:
                path += dummy
            if root.left:
                pre_order(root.left, search_node, path, dummy)
            if root.right:
                pre_order(root.right, search_node, path, dummy)
            dummy.pop()
        p_path, q_path = [], []
        pre_order(root, p,   p_path, [])
        pre_order(root, q,   q_path, [])
        while p_path:
            ans = p_path.pop()
            if ans in q_path:
                return ans
        return -1


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 202 ms
# Your runtime beats 9.25 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right


# Same as above, but it is fail in Python3.x.
# In Python3.x max() will cause 'TypeError: unorderable types: NoneType() > int()', but in Python2.x it is ok.
# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 149 ms
# Your runtime beats 17.19 % of python submissions.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        subs = [self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right)]
        return root if all(subs) else max(subs)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.right = TreeNode(4)
    result = Solution().lowestCommonAncestor(root, root.left, root.right)
    print(result)
