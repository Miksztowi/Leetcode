# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Dijstra
class Solution(object):
    def Dijkstra(self, matrix, vertex):
        """
        :type accounts: List[List[int]]
        :rtype: List[int]
        """

        vertex_counts = len(matrix)
        visited = [False] * vertex_counts
        distance_list = [float('inf')] * vertex_counts
        path = [float('inf')] * vertex_counts
        min_dis_index = 0

        visited[vertex] = True
        for i in range(vertex_counts):
            distance_list[i] = matrix[vertex][i]
            path[i] = vertex

        for i in range(1, vertex_counts):
            min_dis = float('inf')

            for j in range(vertex_counts):
                if not visited[j] and distance_list[j] < min_dis:
                    min_dis = distance_list[j]
                    min_dis_index = j

            visited[min_dis_index] = True

            for k in range(vertex_counts):
                if not visited[k]  \
                        and (matrix[min_dis_index][k] + min_dis) < distance_list[k]:
                    distance_list[k] = matrix[min_dis_index][k] + min_dis
                    path[k] = min_dis_index
        return distance_list


# Bellman_Ford
class Solution1(object):
    def Bellman_Ford(self, matrix, vertex):
        """
        :type accounts: List[List[int]]
        :rtype: List[int]
        """
        vertex_counts = len(matrix)
        path = [False] * vertex_counts
        dist = [float('inf')] * vertex_counts
        dist[vertex] = path[vertex] = 0

        for i in range(vertex_counts - 1):
            for u in range(len(matrix)):
                for v in range(len(matrix[u])):
                    if dist[v] > dist[u] + matrix[u][v]:
                        dist[v] = dist[u] + matrix[u][v]
                        path[v] = u

        for u in range(len(matrix)):
            for v in range(len(matrix[u])):
                if dist[v] > dist[u] + matrix[u][v]:
                    return False

        return dist


# SPFA
import collections
class Solution2(object):
    def Shortest_Path_Faster_Algorithm(self, matrix, vertex):
        """
        :type accounts: List[List[int]]
        :rtype: List[int]
        """
        vertex_counts = len(matrix)
        queue = collections.deque()
        enqueue_counts = [0] * vertex_counts
        path = [float('inf')] * vertex_counts
        dist = [float('inf')] * vertex_counts
        visited = [False] * vertex_counts
        queue.append(vertex)
        dist[vertex] = path[vertex] = 0
        enqueue_counts[vertex] += 1
        visited[vertex] = True

        while queue:
            cur_vertex = queue.popleft()
            visited[cur_vertex] = False

            for j in range(len(matrix[cur_vertex])):
                if dist[j] > dist[cur_vertex] + matrix[cur_vertex][j]:
                    if not visited[j]:
                        if enqueue_counts[j] < vertex_counts - 1:
                            visited[j] = True
                            queue.append(j)
                            enqueue_counts[j] += 1
                            dist[j] = dist[cur_vertex] + matrix[cur_vertex][j]
                        else:
                            return False
        return dist


if __name__ == '__main__':
    # print('The Shortest Path to other vertexs is:', Solution().Dijkstra(
    #     [
    #         [0, 10, float('inf'), float('inf'), float('inf'), 3],
    #         [float('inf'), 0, 7, 5, float('inf'), float('inf')],
    #         [float('inf'), float('inf'), 0, float('inf'), float('inf'), float('inf')],
    #         [3, float('inf'), 4, 0, 7, float('inf')],
    #         [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf')],
    #         [float('inf'), 2, float('inf'), 6, 1, 0],
    #     ],
    #     0
    # ))
    graph = [
                [0, 10, float('inf'), float('inf'), float('inf'), 3],
                [float('inf'), 0, 7, 5, float('inf'), float('inf')],
                [float('inf'), float('inf'), 0, float('inf'), float('inf'), float('inf')],
                [3, float('inf'), 4, 0, 7, float('inf')],
                [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf')],
                [float('inf'), 2, float('inf'), 6, 1, 0],
            ]
    graph = [
                [0, -4, float('inf'), float('inf')],
                [float('inf'), 0, -4, float('inf')],
                [float('inf'), float('inf'), 0, -4],
                [-4, float('inf'), float('inf'), 0]
            ]
    graph = [
                [0, 1, 3],
                [float('inf'), 0, float('inf')],
                [float('inf'), -5, 0],
            ]
    vertex = 0
    print('Graph:')
    for i in range(len(graph)):
        print(['{:^4}'.format(graph[i][j]) for j in range(len(graph[i]))])

    print('Source Vertex:', vertex)
    res = Solution().Dijkstra(graph, vertex)
    print('The Shortest Path to other vertexs is:', res)
    # print(Solution().Bellman_Ford(
    #     [
    #         [0, -10, float('inf'), float('inf'), float('inf'), 3],
    #         [float('inf'), 0, 7, 5, float('inf'), float('inf')],
    #         [float('inf'), float('inf'), 0, float('inf'), float('inf'), float('inf')],
    #         [3, float('inf'), 4, 0, 7, float('inf')],
    #         [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf')],
    #         [float('inf'), 2, float('inf'), 6, 1, 0],
    #     ],
    #     0
    # ))
    # print(Solution().Shortest_Path_Faster_Algorithm(
    #     [
    #         [0, 10, float('inf'), float('inf'), float('inf'), 3],
    #         [float('inf'), 0, 7, 5, float('inf'), float('inf')],
    #         [float('inf'), float('inf'), 0, float('inf'), float('inf'), float('inf')],
    #         [3, float('inf'), 4, 0, 7, float('inf')],
    #         [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf')],
    #         [float('inf'), 2, float('inf'), 6, 1, 0],
    #     ],
    #     0
    # ))


