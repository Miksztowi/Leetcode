# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Bad Solution. Below are other concise solutions.
# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 85 ms
# Your runtime beats 87.56 % of python submissions.
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index])

        def dst_generate(root, left_list, right_list):
            if left_list:
                left_root = len(left_list) // 2
                root.left = dst_generate(TreeNode(left_list[left_root]),
                                         left_list[:left_root], left_list[left_root + 1:])
            if right_list:
                right_root = len(right_list) // 2
                root.right = dst_generate(TreeNode(right_list[right_root]),
                                          right_list[:right_root], right_list[right_root + 1:])

            return root
        dst_generate(root, nums[:root_index], nums[root_index + 1:])
        return root


# Concise, but when iterating it will create many space. And below has solved this problem.
# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 102 ms
# Your runtime beats 26.47 % of python submissions.
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def convert(nums):
            if nums:
                if len(nums) == 1:
                    return TreeNode(nums[0])
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = convert(nums[:mid])
                root.right = convert(nums[mid+1:])
                return root

        return convert(nums)


# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 95 ms
# Your runtime beats 47.95 % of python submissions.
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def convert(nums, lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = convert(nums, lo, mid - 1)
            root.right = convert(nums, mid + 1, hi)
            return root

        return convert(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    print(Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6]))

