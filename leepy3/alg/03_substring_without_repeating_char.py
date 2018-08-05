# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '26/09/2017 10:27 AM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys
from pprint import pprint

app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(app_root)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

from assist import dec

use_trace = True


class Solution(object):
    @staticmethod
    @dec.trace(use_trace)
    def len_of_longest_substring_1(str_in):
        """
        1. 从 s.0 开始, 依次向后统计, 遇到与之前有相同的就停止, 然后从 s.1 重复
        """
        lookup = []
        counter = 0

        for i, s in enumerate(str_in):
            s1 = str_in[i:]
            # print(s1)
            # lookup[i] = max(s1)
            # lookup[counter] = []
            cc = []
            for s_ in s1:
                if s_ in cc:
                    lookup.append(''.join(cc))
                    break
                cc.append(s_)
            counter += 1

        m = max([len(x) for x in lookup])

        for x in lookup:
            if len(x) == m:
                return x

    @staticmethod
    @dec.trace(use_trace)
    def len_of_longest_substring_2(s):
        # 定义字符存储字典, 用来统计是否出现过某个字符
        # res 是返回值, start 为最后一个无重复字符的起始位置
        dic, res, start = {}, 0, 0

        for i, ch in enumerate(s):
            # 如果该字符已经存在, 则更新
            if ch in dic:
                # 更新res为: 取res与当前字符到start间距的最大值
                res = max(res, i - start)
                # 更新 start 为重复字符出现的下一位置
                # 重复字符, 每次都会更新当前位置为最后一次出现的位置
                start = max(start, dic[ch] + 1)

            # 更新 ch 的位置为最后一次出现字符位置
            dic[ch] = i

        # 循环结束, start会指向最后一个无重复字符位置, 然后比较剩余长度与之前计算的最大值
        return max(res, len(s) - start)
        # return res


if __name__ == '__main__':
    sl = Solution()
    # l = sl.lengthOfLongestSubstring('abbdefgoh')
    __ = 'abbdefgh'
    for i in range(1, 3):
        l = getattr(sl, 'len_of_longest_substring_{}'.format(i))(__)
        pprint(l)
