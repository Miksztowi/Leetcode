# -*- encoding:utf-8 -*-
# __author__=='Gan'
import time


class Solution(object):
    def matrixChain(self, nums, n):
        for num in nums:
            if num <= 0:
                return None
        start = time.time()
        product_value_list, product_pos_list = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
        for r in range(2, n):
            for i in range(1, n - r + 1):
                j = i + r - 1
                product_value_list[i][j] = product_value_list[i+1][j] + nums[i-1] * nums[i] * nums[j]
                product_pos_list[i][j] = i

                for k in range(i+1, j):
                    t = product_value_list[i][k] + product_value_list[k+1][j] + nums[i-1] * nums[k] * nums[j]
                    if t < product_value_list[i][j]:
                        product_value_list[i][j] = t
                        product_pos_list[i][j] = k

        def printf(list_):
            for r in range(1, n):
                print('r = {}  '.format(r),
                       ['%8d' % list_[i][i + r - 1] for i in range(1, n - r + 1)])
        print('Matrix Production cost: {}'.format(time.time() - start))

        def gen_path(product_pos_list, start, end, path):
            if start == end:
                path += "A" + str(start)
            elif start + 1 == end:
                path += "(A" + str(start) + '*' +"A" + str(end) + ")"
            else:
                path += '(' + gen_path(product_pos_list, start, product_pos_list[start][end], path) +\
                        gen_path(product_pos_list, product_pos_list[start][end] + 1, end, path) + ')'
            return path

        path = gen_path(product_pos_list, 1, len(nums)-1, '')
        print('The Value of the memo:')
        printf(product_value_list)
        print('The Position of the memo:')
        printf(product_pos_list)
        return path, product_value_list[1][n-1]


if __name__ == '__main__':
    import random
    rand_list = [random.randint(1, 100) for x in range(10)]
    path, res = Solution().matrixChain(rand_list, len(rand_list))
    if res:
        print('The least product times with {} is {}:'.format(path, res))
    else:
        print('Elements must be positive integer.\nPlease input again!')
