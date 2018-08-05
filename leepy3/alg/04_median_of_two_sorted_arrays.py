# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '26/09/2017 2:34 PM'
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


class Solution:
    @dec.trace(1)
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    @staticmethod
    @dec.trace(1)
    def median(list_a, list_b):
        """
        二分查找
        :param list_a:
        :type list_a: list
        :param list_b:
        :type list_b: list
        :return:
        :rtype:
        """
        m, n = len(list_a), len(list_b)
        # 交换 A 为长度小的
        if m > n:
            list_a, list_b, m, n = list_b, list_a, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and list_b[j - 1] > list_a[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and list_a[i - 1] > list_b[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = list_b[j - 1]
                elif j == 0:
                    max_of_left = list_a[i - 1]
                else:
                    max_of_left = max(list_a[i - 1], list_b[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = list_b[j]
                elif j == n:
                    min_of_right = list_a[i]
                else:
                    min_of_right = min(list_a[i], list_b[j])

                return (max_of_left + min_of_right) / 2.0

    @staticmethod
    # @dec.trace(1)
    def find_median(list_a, list_b):
        """
        :param list_a:
        :type list_a: list
        :param list_b:
        :type list_b: list
        :return:
        :rtype:
        """
        # la =  [1, 3, 11, 15]
        # lb = [2, 6, 8]
        # 获取长度, 并置位 list_a 为长度短的list
        m, n = len(list_a), len(list_b)
        # m, n = 4, 3
        if m > n:
            list_a, list_b, m, n = list_b, list_a, n, m
            # = [2,6,8], [1,3,11,15], 3, 4
        # 如果大的 list 为空, raise Error
        if not n:
            raise ValueError

        i_min, i_max, middle = 0, m, (m + n + 1) // 2
        # 0, 3, 3+4+1/2 = 4
        while i_min <= i_max:
            # list_a 从中间开始取值
            i = (i_min + i_max) // 2  # i = 0 + 3 // 2 = 1
            # list_b 中值为 middle - i,
            j = middle - i  # j = 4 - 1 = 3

            # 如果 i 小于 m, 且 左侧 a.x 小于 b.x
            # 1 < 3, la[1] = 6 < lb[2] = 11
            if i < m and list_a[i] < list_b[j - 1]:
                # 如果 la[i] < lb[j-1], 则认为 i_min 过小, 向后移动一位
                i_min = i + 1  # i_min = 1 + 1 = 2
                continue

            # 运行到这里, 已经满足 la[i] > lb[j - 1], 故比较 la[i - 1] 与 lb[j] 的值
            # 如果 la[i]的上一个值 大于 lb[j-1]的下一个值, 则认为 i_max 过大, 向前移动一位
            if i > 0 and list_a[i - 1] > list_b[j]:
                i_max = i - 1
                continue

            # 到这里, i>0, la[i] > lb[j-1] 且 la[i-1] < lb[j], 已经满足条件, 认为是所需要值
            if i == 0:
                # 如果i = 0, 认为 la里最小值, 都比 lb最大值大.
                _left = list_b[j - 1]
            elif j == 0:
                # 则 la 最大值也小于 lb 最小值
                _left = list_a[i - 1]
            else:
                # 取两者之前最大值
                _left = max(list_a[i - 1], list_b[j - 1])

            # 长度为奇数, 则直接使用该值
            if (m + n) % 2 == 1:
                return _left

            # 长度为偶数, 则取left + right 两个值的平均值
            if i == m:
                # la最大值 小于 lb最小值
                _right = list_b[j]
            elif j == n:
                # la最小值 大于 lb最大值
                _right = list_a[i]
            else:
                # 取两者最小值
                _right = min(list_a[i], list_b[j])

            _median = (_left + _right) / 2
            return _median


# la, lb = [1, 3, 5, 7, 9, 11, 13, 15], [2, 4, 6]
la, lb = [1, 3, 11, 15], [2, 6, 8]
# print(Solution().findMedianSortedArrays(la, lb))
# print(Solution().median(la, lb))
print(Solution().find_median(la, lb))

# lc = la + lb
# print(lc)
