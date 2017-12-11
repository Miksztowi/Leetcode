# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 99.64 % of python submissions.
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fre_map = {x: s.count(x) for x in set(s)}  # Avoid to calculate the same element.

        return ''.join(sorted(
            (x * fre_map[x] for x in fre_map), key=len, reverse=True
        ))


if __name__ == '__main__':
    print(Solution().frequencySort('tree'))
    print(Solution().frequencySort('cccaaa'))
    print(Solution().frequencySort('Aabb'))
