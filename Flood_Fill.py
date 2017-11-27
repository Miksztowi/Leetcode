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