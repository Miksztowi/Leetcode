# -*- encoding:utf-8 -*-
# __author__=='Gan'


# An image is represented by a 2-D array of integers, each integer
# representing the pixel value of the image (from 0 to 65535).
# Given a coordinate (sr, sc) representing the starting pixel
# (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
# To perform a "flood fill", consider the starting pixel,
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel),
# and so on. Replace the color of all of the aforementioned pixels with the newColor.
# At the end, return the modified image.


# 277 / 277 test cases passed.
# Status: Accepted
# Runtime: 102 ms
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        visited = [[False for _ in range(len(image[0]))] for _ in
                   range(len(image))]  # Mutable can cause accident error.
        taged = image[sr][sc]

        def dfs(image, sr, sc):
            if image[sr][sc] == taged:
                image[sr][sc] = newColor
            else:
                return
            if sr > 0 and not visited[sr - 1][sc]:
                visited[sr - 1][sc] = True
                dfs(image, sr - 1, sc)
            if sc > 0 and not visited[sr][sc - 1]:
                visited[sr][sc - 1] = True
                dfs(image, sr, sc - 1)
            if sr < len(image) - 1 and not visited[sr + 1][sc]:
                visited[sr + 1][sc] = True
                dfs(image, sr + 1, sc)
            if sc < len(image[0]) - 1 and not visited[sr][sc + 1]:
                visited[sr][sc + 1] = True
                dfs(image, sr, sc + 1)

        dfs(image, sr, sc)
        return image


# 277 / 277 test cases passed.
# Status: Accepted
# Runtime: 132 ms
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def dfs(sr, sc):
            if not (0 <= sr < rows and 0 <= sc < cols) or image[sr][sc] != orig_color:
                return
            image[sr][sc] = newColor
            [dfs(sr + x, sc + y) for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1))]

        if orig_color != newColor:
            dfs(sr, sc)
        return image


if __name__ == '__main__':
    # print(Solution().floodFill(
    #     [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2
    # ))
    # print(Solution().floodFill(
    #     [[0, 0, 0], [0, 1, 0]], 1, 1, 2
    # ))
    print(Solution().floodFill(
        [[0, 0, 0], [0, 1, 0]], 1, 0, 2
    ))
