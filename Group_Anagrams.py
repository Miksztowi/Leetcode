# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of strings, group anagrams together.
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Here is my solution 1 and it's TLE
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = [sorted(str_) for str_ in strs]
        res = []
        appended = []
        for i in range(len(strs)):
            lo = 0
            dummy = []
            while lo < len(strs):
                if sorted_strs[i] == sorted_strs[lo]:
                    if lo not in appended:
                        dummy += strs[lo],
                        appended += lo,

                lo += 1
            if dummy:
                res.append(dummy)
        return res

#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from itertools import groupby
        return [sorted(members) for _, members in groupby(sorted(strs, key=sorted), sorted)]

if __name__ == '__main__':
    print(Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
    print(Solution().groupAnagrams([]))


# 101 / 101 test cases passed.
# Status: Accepted
# Runtime: 296 ms
# Your runtime beats 14.42 % of python submissions.


# Only one line can work out this problem!

# Python solution 1
# Sort and group by group identifier, then sort each group normally.
import itertools
def groupAnagrams(self, strs):
    return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]
# Or "breaking it down" to maybe make it more readable for beginners and
# because I just noticed that in Firefox it violates my self-imposed "no scrollbars" rule
# (I usually use Chrome and didn't think it differed):
def groupAnagrams(self, strs):
    groups = itertools.groupby(sorted(strs, key=sorted), sorted)
    return [sorted(members) for _, members in groups]


# Python solution 2
# Using defaultdict to collect the groups.
import collections
def groupAnagrams(self, strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return map(sorted, groups.values())


# Python solution 3
def anagrams(self, strs):
    count = collections.Counter([tuple(sorted(s)) for s in strs])
    return filter(lambda x: count[tuple(sorted(x))]>1, strs)
# collections.Counter creates a counter object. A counter object is like a specific kind of dictionary
    # where it is build for counting (objects that hashes to same value)
# tuple(sorted(s)) is used here so that anagrams will be hashed to the same value.
    # tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
# filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
# lambda function defined here returns True if number of anagrams of that elements is greater than 1


# Python solution 4
def anagrams(self, strs):
    dic = defaultdict(list)
    map(lambda item: dic[''.join(sorted(item))].append(item), strs)
    return [x for key in dic.keys() for x in dic[key] if len(dic[key]) > 1]
# Equivalent to:
from collections import defaultdict
def anagrams(self, strs):
    dic = defaultdict(list)
    for item in strs:
        after = ''.join(sorted(item))
        dic[after].append(item)
    ans = []
    for item in dic:
        values = dic[item]
        if len(values) > 1:
            ans.extend(values)
    return ans


# Python solution 5
    # And this is the fastest solution in Leetcode. runtime: 188ms.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stats = {}
        for str in strs:
            ordered = ''.join(sorted(str))
            if ordered in stats:
                stats[ordered].append(str)
            else:
                stats[ordered] = [str]
        return list(stats.values())   # Use list() or will get dict_values(values).
