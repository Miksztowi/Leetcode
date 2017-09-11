# -*- encoding:utf-8 -*-
# __author__=='Gan'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, dummpy_dict = 0, 0, {}
        for i, char in enumerate(s):
            if dummpy_dict.get(char):
                while char != s[start]:
                    dummpy_dict[s[start]] = False  # this must above start += 1. To avoid omit start-1
                    start += 1
                start += 1  # To avoid repeat use same char.
            else:
                dummpy_dict[char] = True
            longest = max(longest, i - start + 1)  # Because i begin at 0, so +1 is true length.
        return longest


if __name__ == '__main__':
    test_string_1 = Solution().lengthOfLongestSubstring('aaaaaa')
    test_string_2 = Solution().lengthOfLongestSubstring("bbtablud")
    test_string_3 = Solution().lengthOfLongestSubstring('pwwkew')
    test_string_4 = Solution().lengthOfLongestSubstring("dvdf")
    print(test_string_3)


# 983 / 983 test cases passed.
# Status: Accepted
# Runtime: 102 ms
# Your runtime beats 55.65 % of python submissions.
