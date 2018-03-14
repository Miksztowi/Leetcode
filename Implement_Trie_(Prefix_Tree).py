# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

# 14 / 14 test cases passed.
# Status: Accepted
# Runtime: 244 ms
# Your runtime beats 55.59 % of python3 submissions.
import collections
class TreeNode:
    def __init__(self):
        self.children = collections.defaultdict(TreeNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
