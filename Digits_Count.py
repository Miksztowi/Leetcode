# -*- encoding:utf-8 -*-
# __author__=='Gan'
# 本题与Leetcode无关，是算法课上的习题。
# 一本书的页码从自然数1开始顺序编码直到自然数n。书的页码按照通常的习惯编排，每个页码都不含多余的前导数字0。例如第6页用6表示而不是06或006。
# 数字统计问题要求对给定书的总页码，计算出书的全部页码中分别用到多少次数字0,1,2,3,.....9。


# Solution:
# section_count = num[0]*(m-1)*10^(m-2) and m is the length of num. it's very important.
# digits_dict[i] += 10 ** (num_length - 1)
# digits_dict[int(str_num[0])] += int(str_num[1:] if num_length > 1 else 0) + 1

from datetime import datetime
class Solution(object):
    def digitCount(self, num):
        start = datetime.now()
        digits_dict = dict(zip([x for x in range(10)], [0]*10))
        while True:
            str_num = str(num)
            num_length = len(str_num)

            if num_length - 1 > 0:
                section_count = int(str_num[0]) * (num_length - 1) * (10 ** (num_length - 2))
                print(section_count)
                for i in range(10):
                    digits_dict[i] += section_count

            for i in range(1, int(str_num[0])):
                digits_dict[i] += 10 ** (num_length - 1)

            digits_dict[int(str_num[0])] += int(str_num[1:] if num_length > 1 else 0) + 1

            if num_length - 1 == 0:
                print('Cost {}s'.format(datetime.now() - start))
                return digits_dict

            num = num % (10 ** (num_length - 1))


# Another Problem:  Count the number of k's between 0 and n. k can be 0 - 9.
# Solution:
# If current-bit smaller than k, current count will be added higher-bit multiply the current-bit.
# If current-bit bigger than k, current count will be added higher-bit plus 1 then multiply the current-bit.
# If current-bit equal the k, current count will be added higher-bit multiply the current-bit
# and add the lower-bit plus 1.
class Solution(object):
    def digitCount(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        count = 0
        base = 1
        while num // base:
            higher_bit = num // (base * 10)
            current_bit = num % (base * 10) // base
            lower_bit = num % base

            if current_bit < k:
                count += higher_bit * base
            elif current_bit > k:
                count += (higher_bit + 1) * base
            else:
                count += higher_bit * base + lower_bit + 1
            base *= 10
            print(count)

        return count


if __name__ == '__main__':
    # num = 987654
    # print('num: {}\n'.format(num))
    # print(Solution().digitCount(num))
    num = 5678
    print('num: {}'.format(num))
    print(Solution().digitCount(num, 7))



