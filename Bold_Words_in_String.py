# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a set of keywords words and a string S, make all appearances of all keywords in S bold.
# Any letters between <b> and </b> tags become bold.
# The returned string should use the least number of tags possible,
# and of course the tags should form a valid combination.
# For example, given that words = ["ab", "bc"] and S = "aabcd",
# we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
# Note:
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.


# 72 / 72 test cases passed.
# Status: Accepted
# Runtime: 259 ms
# Leetcode weekly contest 66.
# Set b[i: i + size] to True when word has been matched.After all size has been matched,
# then iterating string to generate answer.
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        if not words:
            return S
        b = [False] * len(S)
        word_max_len = len(max(words, key=len))
        for size in range(1, word_max_len + 1):
            for i in range(len(S) - size + 1):
                if S[i:i + size] in words:
                    b[i:i + size] = [True] * size
        lo, hi = 0, len(S)
        ans = ''
        while lo < hi:
            if b[lo]:
                ans = ans + r'<b>'
                tmp_index = lo
                while lo < hi and b[lo]:
                    lo += 1
                ans = ans + S[tmp_index: lo] + r'</b>'
            else:
                ans = ans + S[lo]
                lo += 1
        return ans

if __name__ == '__main__':
    print(Solution().boldWords(["aab", "bc"], 'aabbcd'))
    print(Solution().boldWords(["aab", "bc"], 'aabcd'))
