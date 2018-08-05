# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '29/09/2017 5:11 PM'
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
    # @return a string
    @dec.trace(1)
    def longest_palindrome(self, s):
        if not isinstance(s, str):
            raise TypeError

        # 原 str 是否已经满足条件
        if s == s[::-1]:
            return s

        max_len = 1
        start = 0

        for i in range(len(s)):
            # 设置本次循环中 判断起始位置
            _current_start = i - max_len
            # 奇数长度情况: 差值 >= 1, 从起始到当前, 是否满足相等
            if _current_start >= 1 and s[_current_start - 1:i + 1] == s[_current_start - 1:i + 1][::-1]:
                # 设置总起始位置为当前位置 - 1
                start = _current_start - 1
                max_len += 2
                continue

            # 偶数长度情况: 差值 >= 0, 从起始到当前, 是否满足相等
            if _current_start >= 0 and s[_current_start:i + 1] == s[_current_start:i + 1][::-1]:
                start = _current_start
                max_len += 1
        # 返回 [起始:起始+长度] 内容
        return s[start:start + max_len]

    # @dec.trace(1)
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


if __name__ == '__main__':
    v = 'cacabba-abababbababa'
    # s = Solution().longest_palindrome(v)
    # print(s)
    s = Solution().longestPalindrome(v)
    print(s)
