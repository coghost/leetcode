# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '25/09/2017 4:17 PM'
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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @staticmethod
    @dec.trace(use_trace)
    def add_two_numbers(l1, l2):
        dummy = n = ListNode(0)

        # 商 + 当前的 val = 进位处理
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            # 取 商 和 余数, 商用来和 next 取和, 余数直接赋值为 val
            # 实际情况来说, carry 或者是0, 或者是1, 可以直接
            carry, val = divmod(carry, 10)

            # 添加到链表数据
            # 首先 n.next 指向 ListNode(val)
            n.next = ListNode(val)
            # 然后 n 指向同一地址, 即指针向next移动
            n = n.next
            # 参考 a=b=c from
            # https://stackoverflow.com/questions/11498441/what-is-this-kind-of-assignment-in-python-called-a-b-true
            # 可以简化为
            # n.next = n = ListNode(val)

        return dummy.next


def num2listnode(num_in):
    """ 输入 num, 返回倒序的 ListNode

    - input: 23
    - output: ListNode(1), ListNode(3), ListNode(2)

    :param num_in:
    :type num_in: int
    :return:
    :rtype:
    """
    l_ = n = ListNode(0)
    num_in = [int(x) for x in str(num_in)]

    for i in reversed(num_in):
        # n.next = n = ListNode(i)
        n.next = ListNode(i)
        n = n.next
    return l_.next


if __name__ == '__main__':
    a = num2listnode(342)
    b = num2listnode(465)
    s = Solution()
    rs = s.add_two_numbers(a, b)
    while rs:
        print('{}'.format(rs.val), end=' -> ' if rs.next else '')
        rs = rs.next
