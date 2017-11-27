# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right, negative meaning left).
# Find out the state of the asteroids after all collisions. If two asteroids meet,
# the smaller one will explode. If both are the same size, both will explode.

# Leetcode Contest 60.
# 275 / 275 test cases passed.
# Status: Accepted
# Runtime: 159 ms
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) <= 1:
            return asteroids
        left, right = 1, len(asteroids)
        while left < right:
            if left > 0 and asteroids[left - 1] > 0 > asteroids[left] and asteroids[left - 1] * asteroids[left] < 0:
                collision = asteroids[left - 1] + asteroids[left]
                if collision > 0:
                    asteroids.pop(left)
                elif collision < 0:
                    asteroids.pop(left - 1)
                    left -= 1
                else:
                    asteroids.pop(left - 1)
                    asteroids.pop(left - 1)
                    left -= 1
                    right -= 1
                right -= 1
            else:
                left += 1
        return asteroids


# 275 / 275 test cases passed.
# Status: Accepted
# Runtime: 79 ms
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for asteroid in asteroids:
            if asteroid > 0:
                ans += asteroid,
            else:
                while len(ans) > 0 and ans[-1] > 0:
                    if asteroid + ans[-1] > 0:
                        break
                    elif asteroid + ans[-1] == 0:
                        ans.pop()
                        break
                    else:
                        ans.pop()
                else:
                    ans += asteroid,
        return ans


if __name__ == '__main__':
    print(Solution().asteroidCollision([2, 10, -5]))
    print(Solution().asteroidCollision([10, 2, -5]))
    print(Solution().asteroidCollision([8, -8]))
    print(Solution().asteroidCollision([2, 10]))
    print(Solution().asteroidCollision([10, 2, -5, -5, -17]))
    print(Solution().asteroidCollision([-2, -2, 1, -2]))
    print(Solution().asteroidCollision([1, -2, 1, 1]))
    print(Solution().asteroidCollision([1, 1, -1, -2]))
    print(Solution().asteroidCollision([-1, 1, 1, -1, -2]))
