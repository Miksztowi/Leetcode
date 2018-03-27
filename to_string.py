# -*- coding:utf-8 -*-

def to_string(digit):
    if digit == 0:
        return '0'

    if digit < 0:
        sign = '-'
        digit = abs(digit)
    else:
        sign = '+'

    tmp_str = []
    while digit:
        tmp = digit % 10
        digit //= 10
        tmp_str += chr(tmp + 48)

    return sign + ''.join(tmp_str[::-1])

if __name__ == '__main__':
    assert to_string(30) == '+30'
    assert to_string(1) == '+1'
    assert to_string(11) == '+11'
    assert to_string(111) == '+111'
    assert to_string(0) == '0'
    assert to_string(-10) == '-10'