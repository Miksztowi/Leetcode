# -*- encoding:utf-8 -*-
# __author__=='Gan'
# 本题是算法课上的习题，与Leetcode无关。
# 给定一个以字符串形式表示的入栈序列，请求出一共有多少种可能的出栈顺序？如何输出所有可能的出栈序列？
# 比如入栈序列为：1 2 3  ，则出栈序列一共有五种，分别如下：1 2 3、1 3 2、2 1 3、2 3 1、3 2 1


from time import time

# Catalan!!!!!
# https://github.com/vo01github/Math/tree/master/%E7%BB%84%E5%90%88%E6%95%B0%E5%AD%A6/%E5%8D%A1%E7%89%B9%E5%85%B0%E6%95%B0
# https://zh.wikipedia.org/wiki/%E6%AC%A7%E4%BB%81%C2%B7%E6%9F%A5%E7%90%86%C2%B7%E5%8D%A1%E7%89%B9%E5%85%B0
class Solution(object):
    def OrderStack(self, num):
        """
        :type num:  n
        :rtype: List[int]
        """
        res = []
        start = time()

        def dfs(sum, path, res):
            if sum < 0:
                return
            if len(path) == num * 2:
                if sum == 0:
                    res.append(path)
                return
            dfs(sum - 1, path + [-1], res)
            # Use the -1 and 1 for easy traverse and judgement.
            # Of course,the 1 and 0 are ok.
            dfs(sum + 1, path + [1], res)
        dfs(0, [], res)

        for r in res:
            dummy = [x for x in range(1, num+1)]
            pop_queue = []
            push_stack = []
            for i in r:
                if i == -1:
                    pop_queue += push_stack.pop(),
                else:
                    push_stack += dummy.pop(0),
            print(pop_queue)
        print('The traverse has cost {}s'.format(time() - start))

if __name__ == '__main__':
    print(Solution().OrderStack(10))
