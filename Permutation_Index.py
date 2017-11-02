# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a permutation which contains no repeated number, find its index in all the permutations of these numbers,
# which are ordered in lexicographical order. The index begins at 1.

# Solution:
# Iterative to count from i to len(A) that how much number smaller than A[i] , then multiply flips[len(A) - 1 - i].
class Solution():
    def permutationIndex(self, A):
        """
        @param: A: An array of integers
        @return: A long integer
        """
        # write your code here
        if not A:
            return 1

        flips = [x for x in range(0, len(A) + 1)]
        for i in range(1, len(A)):
            flips[i + 1] *= flips[i]
        index = 0
        for i in range(len(A)):
            count = 0
            for j in range(i, len(A)):
                if A[i] >= A[j]:  # From i to len(A) to find how much number smaller than A[i].
                    count += 1
            index += (count - 1) * flips[len(A) - 1 - i]

        return index + 1


if __name__ == '__main__':
    print(Solution().permutationIndex([3, 2, 6, 7, 4, 5, 1]))
