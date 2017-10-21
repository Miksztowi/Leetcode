# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            dummy = preorder.pop(0)
            index_ = inorder.index(dummy)
            root = TreeNode(dummy)
            root.left = self.buildTree(preorder, inorder[:index_])
            root.right = self.buildTree(preorder, inorder[index_+1:])
            return root


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (preorder or inorder):
            return None
        root = TreeNode(preorder[0])
        nodes_stack = [root]
        node_index, level_index = 1, 0
        while node_index < len(preorder):
            temp_node = nodes_stack[-1]
            if temp_node.val != inorder[level_index]:
                temp_node.left = TreeNode(preorder[node_index])
                nodes_stack.append(temp_node.left)
                node_index += 1
            else:
                nodes_stack.pop()
                level_index += 1
                if not nodes_stack or nodes_stack[-1].val != inorder[level_index]:
                    temp_node.right = TreeNode(preorder[node_index])
                    nodes_stack.append(temp_node.right)
                    node_index += 1

        return root


if __name__ == '__main__':
    print(Solution().buildTree([1, 2, 3, 4, 5, 6],
                               [3, 2, 4, 1, 5, 6]))


