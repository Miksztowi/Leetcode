# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a string and a string dictionary, find the longest string in the dictionary
# that can be formed by deleting some characters of the given string. If there are more than one possible results,
# return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 986 ms
# Your runtime beats 33.33 % of python3 submissions.
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not (s and d):
            return ''
        d.sort(key=len, reverse=True)
        max_length = 0
        res = ''
        for i in d:
            s_len = 0
            i_len = 0
            while s_len < len(s) and i_len < len(i):
                if i[i_len] == s[s_len]:
                    i_len += 1
                    s_len += 1
                else:
                    s_len += 1
            if i_len == len(i):
                if max_length > i_len:
                    return res
                elif max_length < i_len:
                    max_length = i_len
                    res = i
                else:
                    res = min(res, i)
        return res

# iter()
# The built-in function iter() takes an iterable object and returns an iterator.
# To remember the state when during iteration,
# c in it returns True if the value in the iteration and updates the state to point at the next value
# return False when it goes to the end of iteration

# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 196 ms
# Your runtime beats 88.25 % of python submissions.
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def is_subsequence(x):
            it = iter(s)
            return all(_ in it for _ in x)
        return min(list(filter(is_subsequence, d)) + [''], key=lambda x: (-len(x), x))

# Return the first valid one without testing the rest.
# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 209 ms
# Your runtime beats 84.20 % of python submissions.
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(_ in it for _ in x):
                return x
        return ''


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 192 ms
# Your runtime beats 89.98 % of python submissions.
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def is_subsequence(x):
            it = iter(s)
            return all(_ in it for _ in x)
        d.sort(key=lambda x: (-len(x), x))
        # filter() will return the same type as iterator, else return a list.
        # But next(iterator[, default]) need iterator.
        # so return next(iter(filter(is_subsequence, d)), '')
        return next(filter(is_subsequence, d), '')


if __name__ == '__main__':
    print(Solution().findLongestWord('abpcplea', ["ale", "apple", "monkey", "plea"]))
    print(Solution().findLongestWord('abpcplea', ["a", "b", "c"]))