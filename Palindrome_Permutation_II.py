# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be form.
# For example:
# Given s = "aabb", return ["abba", "baab"].
# Given s = "abc", return [].


# Approach 1 Brute Force [Time Limit Exceeded]
class Solution(object):
    def palindromePerm(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_palindrome(s):
            for i in range(len(s)):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

        def permute(s, begin):
            if begin == len(s):
                dummy_string = ''.join(s)
                if is_palindrome(dummy_string):
                    self.result.add(dummy_string)

            else:
                for i in range(begin, len(s)):
                    s[i], s[begin] = s[begin], s[i]
                    permute(s, begin + 1)
                    s[i], s[begin] = s[begin], s[i]

        self.result = set()  # Use set() to eliminate the duplicates.
        permute([x for x in s], 0)
        return self.result


# Solution:
# One idea to do so is to generate only the first half of the palindromic string and to append its reverse string to
# itself to generate the full length palindromic string.
# In case of a string s with odd length, whose palindromic permutations are possible, one of the characters in s must
# be occurring an odd number of times. We keep a track of this character, ch, and it is kept separate from the st. We
# again generate the permutations for st similarly and append the reverse of the generated permutation to itself, but we
# also place the character ch at the middle of the generated string.
# Approach 2 Backtracking [Accepted]
class Solution(object):
    def palindromePerm(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ascii_dict = {}
        count = 0
        for i in s:
            ascii_dict[i] = ascii_dict.get(i, 0) + 1
            if ascii_dict[i] % 2:
                count += 1
            else:
                count -= 1

        def permute(s, begin, ch):
            if begin == len(s):
                string = ''.join(s)
                reverse_string = ''.join(s[::-1])
                self.result.append(string + ch + reverse_string)
            else:
                for i in range(begin, len(s)):
                    if s[i] != s[begin] or i == begin:
                        s[i], s[begin] = s[begin], s[i]
                        permute(s, begin + 1, ch)
                        s[i], s[begin] = s[begin], s[i]

        if 0 <= count <= 1:
            ch = ''
            permutation_list = []
            for key in ascii_dict:
                if ascii_dict[key] % 2:
                    ch = key
                for i in range(ascii_dict[key] // 2):
                    permutation_list += key,

            self.result = []
            permute(permutation_list, 0, ch)
            return self.result

        else:
            return []


if __name__ == '__main__':
    print(Solution().palindromePerm('aabb'))
    print(Solution().palindromePerm('a'))
    print(Solution().palindromePerm('ab'))








