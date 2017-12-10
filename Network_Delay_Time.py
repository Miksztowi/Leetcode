# -*- encoding:utf-8 -*-
# __author__=='Gan'


# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node,
# and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
# If it is impossible, return -1.
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.


# 51 / 51 test cases passed.
# Status: Accepted
# Runtime: 102 ms
import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        nodes = collections.defaultdict(dict)
        Q = set(range(N))
        dist = [float('inf')] * N
        dist[K - 1] = 0

        for u, v, w in times:
            nodes[u - 1][v - 1] = w

        while Q:
            u = None
            for node in Q:
                if u is None or dist[node] < dist[u]:
                    u = node
            Q.remove(u)
            for v in nodes[u]:
                alt = dist[u] + nodes[u][v]
                if dist[v] > alt:
                    dist[v] = alt
        ans = max(dist)
        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    print(Solution().networkDelayTime(
        [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
        4,
        2
    ))
