# -*- encoding:utf-8 -*-
# __author__=='Gan'



# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
# Example 1:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 176 / 176 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 99.18 % of python submissions.
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def hash_strings(node):
            return '*' + str(node.val) + '^' + hash_strings(node.left) + hash_strings(node.right) if node else '@'

        return hash_strings(t) in hash_strings(s)


# 176 / 176 test cases passed.
# Status: Accepted
# Runtime: 342 ms
# Your runtime beats 77.21 % of python submissions.
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def is_match(s_node, t_node):
            if not (s_node and t_node):
                # return True is error
                return s_node is t_node
            return s_node.val == t_node.val and \
                is_match(s_node.left, t_node.left) and is_match(s_node.right, t_node.right)

        def is_subtree(s_node, t_node):
            if not s_node:
                return False
            if is_match(s_node, t_node):
                return True
            return is_subtree(s_node.left, t_node) or is_subtree(s_node.right, t_node)

        return is_subtree(s, t)


# 176 / 176 test cases passed.
# Status: Accepted
# Runtime: 195 ms
# Your runtime beats 80.98 % of python submissions.
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        from hashlib import sha256
        def hash_string(x):
            S = sha256()
            S.update(x.encode())
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            merkle_left = merkle(node.left)
            merkle_right = merkle(node.right)
            node.merkle = hash_string(merkle_left + str(node.val) + merkle_right)
            return node.merkle

        def dfs(node):
            if not node:
                return node is t
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        merkle(s)
        merkle(t)
        return dfs(s)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.right = TreeNode(2)

    subtree = TreeNode(4)
    subtree.left = TreeNode(1)
    subtree.right = TreeNode(2)
    print(Solution().isSubtree(root, subtree))
    print(Solution().isSubtree(None, None))
