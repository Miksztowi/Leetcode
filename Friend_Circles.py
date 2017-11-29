# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
# and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

# Whenever we see a list of pairs as input, one probable approach will be to treat that as a list of edges and model
# the question as a graph. In this question, the idea here is to connect words to their similar words, and all
# connected words are similar. In each connected component of a graph, select any word to be the root word and
# then generate a mapping of word to root word. If two words are similar, they have the same root word.
# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# Your runtime beats 53.47 % of python submissions.
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        friend_cricles = {}

        def dfs(kid, root_kid):
            if kid in friend_cricles:
                return
            friend_cricles[kid] = root_kid
            [dfs(k, root_kid) for k in range(len(M)) if M[kid][k]]

        for kid in range(len(M)):
            dfs(kid, kid)
        return len({friend_cricles[c] for c in friend_cricles})


# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 96 ms
# Your runtime beats 23.33 % of python submissions.
import collections
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        friends = {}
        rank = collections.defaultdict(int)

        def find(kid):
            if friends[kid] == kid:
                return kid
            friends[kid] = find(friends[kid])
            return friends[kid]

        def union(kid1, kid2):
            friend1 = find(kid1)
            friend2 = find(kid2)
            if rank[friend1] > rank[friend2]:
                friends[friend2] = friend1
            elif rank[friend1] < rank[friend2]:
                friends[friend1] = friend2
            else:
                friends[friend2] = friend1
                rank[friend1] += 1

        for i in range(len(M)):
            friends[i] = i

        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] and i != j:
                    union(i, j)

        return len({find(c) for c in friends})


if __name__ == '__main__':
    print(Solution().findCircleNum(
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    ))

    print(Solution().findCircleNum(
        [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    ))

    print(
        Solution().findCircleNum(
            [[1, 1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
        )
    )
