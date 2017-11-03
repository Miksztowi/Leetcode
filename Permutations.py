# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 75 ms
# Your runtime beats 34.78 % of python submissions.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            dummy = []
            for perm in res:
                for i in range(len(perm)+1):
                    dummy.append(perm[:i] + [num] + perm[i:])
            res = dummy
        return res


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        l = list(permutations(nums))

        return l


# If you're using an older Python (<2.6) for some reason or are just curious to know how it works,
# here's one nice approach, taken from http://code.activestate.com/recipes/252178/:
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


# A couple of alternative approaches are listed in the documentation of itertools.permutations. Here's one:
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


# And another, based on itertools.product:
from itertools import product
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Your runtime beats 59.84 % of python submissions.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def permute(nums, begin):
            if begin >= len(nums):
                self.result += nums[:],
            for i in range(begin, len(nums)):
                nums[begin], nums[i] = nums[i], nums[begin]
                permute(nums, begin + 1)
                nums[begin], nums[i] = nums[i], nums[begin]

        self.result = []
        permute(nums, 0)

        return self.result


if __name__ == '__main__':
    print(Solution().permute([x for x in range(3)]))

