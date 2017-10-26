# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 199 ms
# Your runtime beats 68.01 % of python submissions.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            root = TreeNode(postorder.pop())
            index_ = inorder.index(root.val)
            root.right = self.buildTree(inorder[index_+1:], postorder)
            root.left = self.buildTree(inorder[:index_], postorder)
            return root


# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 49 ms
# Your runtime beats 99.70 % of python submissions.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and postorder):
            return []
        node_index = len(postorder) - 2
        level_index = len(postorder) - 1
        root = TreeNode(postorder[-1])
        node_stack = [root]
        while node_index > -1:
            temp_node = node_stack[-1]
            if temp_node.val != inorder[level_index]:
                temp_node.right = TreeNode(postorder[node_index])
                node_stack.append(temp_node.right)
                node_index -= 1
            else:
                node_stack.pop()
                level_index -= 1
                if not node_stack or node_stack[-1].val != inorder[level_index]:
                    temp_node.left = TreeNode(postorder[node_index])
                    node_stack.append(temp_node.left)
                    node_index -= 1
        return root


if __name__ == '__main__':
    print(Solution().buildTree([3, 2, 4, 1, 5, 6],
                               [3, 4, 2, 6, 5, 1]))




