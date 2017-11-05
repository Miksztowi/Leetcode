# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order.
# If there is no answer, return the empty string.


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res_set, res_word = {''}, ''

        for word in sorted(words):
            if word[:-1] in res_set:
                res_set.add(word)
                res_word = max(res_word, word, key=len)  # When a == b, max(a, b, key=len) will return a.
        return res_word


if __name__ == '__main__':
    print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))
    print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print(Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))
    print(Solution().longestWord(["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]))
