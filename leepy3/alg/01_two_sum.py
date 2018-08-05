# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '21/09/2017 4:06 PM'
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

use_trace = True


class Solution:
    @staticmethod
    @dec.trace(use_trace)
    def two_sum1(nums, target):
        """循环遍历

        - n * n => O(n²)

        :param nums:
        :type nums:  list
        :param target:
        :type target: int
        :return:
        :rtype:
        """
        for i, iv in enumerate(nums):
            # T = n
            for j, jv in enumerate(nums[i:]):
                # T = n
                if iv + jv == target:
                    return i, i + j

    @staticmethod
    @dec.trace(use_trace)
    def two_sum2(nums, target):
        # O(n)
        for i, v in enumerate(nums):
            # t 为 差值
            t = target - v
            # 如果 差值在数组中, 则成功
            if t in nums[i:]:
                return i, nums.index(t)

    @staticmethod
    @dec.trace(use_trace)
    def two_sum3(nums, target):
        # 待查询 dict
        lookup = {}
        for i, v in enumerate(nums):
            # 如果差值在字典中存在, 则返回差值key对应的值: 索引
            if target - v in lookup:
                return lookup[target - v], i
            # 以当前值为 key, 记录当前值对应的索引
            lookup[v] = i

    @staticmethod
    @dec.trace(use_trace)
    def two_sum4(nums, target):
        """使用字典方式, 时间复杂度与 two_sum3 一致

        区别:

        - two_sum3, 使用当前值为 key
        - two_sum4, 使用差值为 key

        :param nums:
        :type nums:
        :param target:
        :type target:
        :return:
        :rtype:
        """
        lookup = {}
        for i, v in enumerate(nums):
            if v in lookup:
                return lookup[v], i
            lookup[target - v] = i


"""
the output is:
------
two_sum1: (456, (18, 19))
two_sum2: (58, (18, 19))
two_sum3: (61, (18, 19))
two_sum4: (61, (18, 19))
"""
if __name__ == '__main__':
    _arr_in = [2, 7, 11, 19, 17, 3, 4, 5, 6, 7, 8, 9, 10, 13, 212, 129, 1, 12, 18, 15]
    _target = 33
    s = Solution()
    for i__ in range(1, 5):
        print('two_sum{}:'.format(i__), getattr(s, 'two_sum{}'.format(i__))(_arr_in, _target))
