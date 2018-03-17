# -*- encoding:utf-8 -*-
# __author__=='Gan'

# 实现一个函数，根据标题序列生成相应的标题序号。
# 输入参数，一个 Array，每个元素都是 # 为前缀的标题，保证层级连续，然后返回解析好的数据结构。
# 输入
# ["# a", "## b", "## c", "### d", "# e"]
#
#
# 输出
# [{"hn": "1", "title": "a"},
# {"hn": "1.1", "title": "b"},
# {"hn": "1.2", "title": "c"},
# {"hn": "1.2.1", "title": "d"},
# {"hn": "2", "title": "e"}]

class Solution(object):
    def markdown_parser(self, titles):
        """
        :type titles: List
        :rtype: List
        """
        idxs = [1]  # 控制标题级别
        nums = [0]  # 保存标题对应的编号
        res = []
        for title in titles:
            idx = title.index(' ')
            if idx not in idxs:
                nums.append(1)
                idxs.append(idx)
            else:
                nums[idx - 1] += 1
            hn = '.'.join([str(x) for x in nums[:idx]])
            res.append({"hn": hn, "title": title[idx + 1]})
        return res


if __name__ == '__main__':
    print(Solution().markdown_parser(
        ["# a", "## b", "## c", "### d", "# e"]
    ))
    print( Solution().markdown_parser(["# a", "# b", "# c", "# d", "# e"]))
    print( Solution().markdown_parser(["# a", "## b", "## c", "### d", "## e"]))
    assert Solution().markdown_parser(["# a", "## b", "## c", "### d", "# e"]) == [{"hn": "1", "title": "a"},{"hn": "1.1", "title": "b"},{"hn": "1.2", "title": "c"},{"hn": "1.2.1", "title": "d"},{"hn": "2", "title": "e"}]
    assert Solution().markdown_parser(["# a", "# b", "# c", "# d", "# e"]) == [{'hn': '1', 'title': 'a'}, {'hn': '2', 'title': 'b'}, {'hn': '3', 'title': 'c'}, {'hn': '4', 'title': 'd'}, {'hn': '5', 'title': 'e'}]