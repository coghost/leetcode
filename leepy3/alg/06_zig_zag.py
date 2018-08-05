# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '16/10/2017 2:43 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys

app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(app_root)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

from assist import dec


class ZigZag(object):
    # @dec.trace(1)
    def convert_me(self, s='PAYPALISHIRING', num_rows=3):
        """
        input: PAYPALISHIRING
        output:
            P   A   H   N
            A P L S I I G
            Y   I   R

        return PAHNAPLSIIGYIR

        :param s:
        :type s:
        :param num_rows:
        :type num_rows:
        :return:
        :rtype:
        """
        out_ = [[' ' for _ in range(len(s))] for __ in range(num_rows)]
        for i, s_ in enumerate(s):
            m = i % 4
            if m == 0:
                out_[m][i] = s_
            if m in [1, 3]:
                out_[m % 2][i - 1] = s_
            if m == 2:
                out_[m][i - 2] = s_

        for o in out_:
            print(''.join(o))

        return ''.join(''.join(o_) for o_ in out_).replace(' ', '')

    def convert(self, s='PAYPALISHIRING', num_rows=3):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        if num_rows == 1 or num_rows > len(s):
            return s

        rs = [''] * num_rows
        idx, step = 0, 1
        for x in s:
            rs[idx] += x
            if not idx:
                step = 1
            elif idx == num_rows - 1:
                step = -1
            idx += step

        return ''.join(rs)


if __name__ == '__main__':
    zz = ZigZag()
    s_ = zz.convert()
    print(s_)
    # a = [''] * 3
    # print(a)
