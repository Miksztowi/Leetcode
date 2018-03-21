# -*- encoding:utf-8 -*-
# __author__=='Gan'

# 驼峰字符串转蛇形字符串

def transform(str_):
    upper_idxs = [0]
    res = []
    for i, s in enumerate(str_):
        if s.isupper():
            upper_idxs += i,
    upper_idxs += len(str_),
    lower_str = str_.lower()
    for i, b in zip(upper_idxs, upper_idxs[1:]):
        res += lower_str[i: b],
    return '_'.join(res)


if __name__ == '__main__':
    print(transform('findById'))
    print(transform(''))


