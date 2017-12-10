# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Leetcode Weekly Contest 62.
# Given a binary tree where every node has a unique value, and a target key k,
# find the closest leaf node to target k in the tree.
# A node is called a leaf if it has no children.
# In the following examples, the input tree is represented in flattened form row by row.
# The actual root tree given will be a TreeNode object.
# Example 1:
# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2
# Output: 2 (or 3)
# Explanation: Either 2 or 3 is the closest leaf node to 1.
# Example 2:
# Input:
# root = [1], k = 1
# Output: 1
# Explanation: The closest leaf node is the root node itself.
# Example 3:
# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
# Output: 3
# Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.
# Note:
# root represents a binary tree with at least 1 node and at most 1000 nodes.
# Every node has a unique node.val in range [1, 1000].
# There exists some node in the given binary tree for which node.val == k.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 335 / 335 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Treat binary tree as the undirected graphs.
# Perform BFS from the target node to find the closest leaf node.
import collections
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        graphs = collections.defaultdict(list)
        leaves = []
        stack = [k]
        visited = {k}

        # Undirected Graphs Construction.
        def construction(node):
            if node.left:
                graphs[node.val].append(node.left.val)
                graphs[node.left.val].append(node.val)
                construction(node.left)
            if node.right:
                graphs[node.val].append(node.right.val)
                graphs[node.right.val].append(node.val)
                construction(node.right)
            if not (node.left or node.right):
                leaves.append(node.val)

        construction(root)
        # print(graphs)


        while stack:
            next_level = []
            for node in stack:
                if node in leaves:
                    return node
                for neighbor in graphs[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_level.append(neighbor)

            stack = next_level


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    print(Solution().findClosestLeaf(root, 2))
    print(Solution().findClosestLeaf(TreeNode(1), 1))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(7)
    root.right.right.right.left = TreeNode(10)
    root.right.left.left = TreeNode(6)
    root.right.left.left.left = TreeNode(8)
    root.right.left.left.right = TreeNode(9)
    print(Solution().findClosestLeaf(root, 3))
    print(Solution().findClosestLeaf(root, 7))
