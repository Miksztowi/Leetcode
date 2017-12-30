# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 1572 ms
# Your runtime beats 17.66 % of python submissions.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def helper(root, val):
            if root:
                return int(root.val == val) + helper(root.left, val - root.val) + helper(root.right, val - root.val)
            return 0

        if root:
            return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 69 ms
# Your runtime beats 86.40 % of python submissions.
# Using hash-map to record node's sum of paths.
# @gabbu:
# Two Sum Method: Optimized Solution
# A more efficient implementation uses the Two Sum idea. It uses a hash table (extra memory of order N). With more space, it gives us an O(N) complexity.
# As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (sum_so_far (prefix) + N.val). in hash-table. Note this sum is the sum from root to N.
# Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
# How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
# Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.
class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def helper(root, cache, last_sum, target):
            if root:
                cur_sum = last_sum + root.val
                complement = cur_sum - target
                if complement in cache:
                    result.append(cache[complement])
                cache.setdefault(cur_sum, 0)
                cache[cur_sum] += 1
                helper(root.left, cache, cur_sum, target)
                helper(root.right, cache, cur_sum, target)
                cache[cur_sum] -= 1

        result = []
        helper(root, dict({0: 1}), 0, sum_)
        return sum(result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().pathSum(root, 3))
    print(Solution().pathSum(TreeNode(1), 1))
