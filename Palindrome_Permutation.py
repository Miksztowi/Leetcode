# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a string, determine if a permutation of the string could form a palindrome.
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

# Solution:
# If a string with an even length is a palindrome, every character in the string must always occur an even number of
# times. If the string with an odd length is a palindrome, every character except one of the character must always occur
# an even numbers of times. Thus, in case of a palindrome, the number of characters with odd number of occurences can't
# exceed 1(1 in case of odd length and 0 in case of even length).


# Approach #1 Brute Force [Accepted]
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        for i in range(128):
            dummy = 0
            for j in s:
                if ord(j) == i:
                    dummy += 1
            count += dummy % 2
        return count <= 1


# Approach #2 Using HashMap [Accepted]
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ascii_dict = {}
        count = 0
        for i in s:
            ascii_dict[i] = ascii_dict.get(i, 0) + 1
        for i in ascii_dict:
            if ascii_dict[i] % 2:
                count += 1
                if count > 1:
                    return False
        return count <= 1


# Approach #3 Using Array [Accepted]
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ascii_nums = [0] * 128
        count = 0
        for i in s:
            ascii_nums[ord(i)] += 1

        for i in ascii_nums:
            if i % 2:
                count += 1
                if count > 1:
                    return False
        return count <= 1


# Approach #4 Single Pass [Accepted]:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ascii_dict = {}
        count = 0
        for i in s:
            ascii_dict[i] = ascii_dict.get(i, 0) + 1
            if ascii_dict[i] % 2:
                count += 1
            else:
                count -= 1
        return count <= 1


# Approach #5 Using Set [Accepted]:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ascii_set = set()
        for i in s:
            if ascii_set.issuperset([i]):
                ascii_set.remove(i)
            else:
                ascii_set.add(i)

        return len(ascii_set) <= 1


if __name__ == '__main__':
    print(Solution().isPalindrome('code'))
    print(Solution().isPalindrome('aab'))
    print(Solution().isPalindrome('carerac'))

