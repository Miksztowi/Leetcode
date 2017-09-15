# -*- encoding:utf-8 -*-
# __author__=='Gan'

# 今天逛老师的博客，看到了一道有趣的算法题。所以拿来写一下啦。
# 题目描述：给一个包含非负整数的数组(长度为n)，找出由这些数字组成的最大的3的倍数，没有的话则输出impossible。
# 例如，如果输入的数组为{8,1,9}，输出应为“9 8 1”，并且如果输入的数组为{8,1,7,6,0}，输出应为”8760″。


class Solution(object):
    def maxMultipleOfThree(self, nums):
        """
        :type nums: list
        :rtype: list
        """
        res_nums, sum_ = [], 0
        remain_0_list = []
        remain_1_list = []
        remain_2_list = []
        nums.sort()
        if len(nums) < 1 :
            return ""
        for num in nums:
            sum_ += num
            if num % 3 == 1:
                remain_1_list.append(num)
            elif num % 3 == 2:
                remain_2_list.append(num)
            else:
                remain_0_list.append(num)
        if sum_ % 3 == 2:
            if sum(remain_1_list[-2:]) > remain_2_list[-1]:
                remain_2_list.pop()
            else:
                remain_1_list.pop()
                remain_1_list.pop()
        elif sum_ % 3 == 1:
            remain_1_list.pop()
        res_nums = remain_0_list + remain_1_list + remain_2_list
        res_nums.sort()
        if res_nums[-1] == 0:
            return ""
        else:
            return "".join([str(x) for x in res_nums[::-1]])


if __name__ == '__main__':
    print(Solution().maxMultipleOfThree([9,8,1,0,0,0,6,7]))
    print(Solution().maxMultipleOfThree([0,0]))
    print(Solution().maxMultipleOfThree([]))

