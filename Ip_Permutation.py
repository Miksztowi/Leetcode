# -*- encoding:utf-8 -*-
# __author__=='Gan'

# notes: 1.递归和非递归 2.不允许遍历 3.开始时间和结束时间 4.无需检查字符串合法性，需要检查有效性. 5.前导'0'


# DFS 递归。
class Solution:
    def permutation(self, string):
        """
        :type string: str
        :rtype: None  # 不需要返回结果，只需要打印合法结果即可
        """
        if len(string) < 4 or len(string) > 12:
            return None

        def dfs(s, path, tmp):
            if path == 4:
                if s != '':
                    return
                print('.'.join(tmp))
            else:
                for i in range(min(3, len(s) - 3 + path)):
                    if not (i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0'):
                        dfs(s[i + 1:], path + 1, tmp + [s[:i + 1]])

        dfs(string, 0, [])


# 用栈 非递归。
class Solution:
    def permutation(self, string):
        """
        :type string: str
        :rtype: None  # 不需要返回结果，只需要打印合法结果即可
        """
        if len(string) < 4 or len(string) > 12:
            return None

        S = [([], string)]  # 初始化栈
        while S:
            path, s = S.pop()
            if len(path) == 4:
                if s == '':
                    print('.'.join(path))
                continue
            for i in range(min(3, len(s) - 3 + len(path))):
                if not (i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0'):
                    S.append((path + [s[:i + 1]], s[i + 1:]))


if __name__ == '__main__':
    result1 = Solution().permutation('123452')
    result2 = Solution().permutation('1000000000')
    result3 = Solution().permutation('1112134523223')
    result4 = Solution().permutation('7777777777777')
    result5 = Solution().permutation('1234')
    result6 = Solution().permutation('00000')  # '0'处理
