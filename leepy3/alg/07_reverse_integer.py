# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '17/10/2017 6:29 PM'
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


class ReverseInt(object):
    def reverse(self, x):
        if x < 0:
            return -self.reverse(-x)

        res = 0
        while x:
            x, y = divmod(x, 10)
            res = res * 10 + y

        return res if res <= 0x7fffffff else 0


if __name__ == '__main__':
    ri = ReverseInt()
    print(ri.reverse(123456789))
