# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '16/10/2017 3:19 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys
import random

app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(app_root)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')


class IncUrl(object):
    def __init__(self):
        self.max_len = 6
        self.url_pre = 'https://tinyc.cn/'
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.ltos = {}
        self.stol = {}
        self.counter = 1

    def long2short(self, url):
        __url_s = self.base102alpha(self.counter)
        self.ltos[url] = self.counter
        self.stol[self.counter] = url
        self.counter += 1
        return self.url_pre + __url_s

    def short2long(self, url):
        url = url[len(self.url_pre):]
        n = self.alpha2base10(url)
        return self.stol[n]

    def alpha2base10(self, s):
        n = 0
        for x in s:
            n = n * 62 + self.convert(x)
        return n

    def convert(self, c):
        return self.alphabet.find(c)

    def base102alpha(self, n):
        al = ['0' for _ in range(6)]
        __i = 5
        while n:
            # print(n % 62)
            al[__i] = self.alphabet[n % 62]
            __i -= 1
            n //= 62

        return ''.join(al)


class RandUrl(object):
    def __init__(self, trim_confused=False):
        """
        if enable trim_confused
            will trim 8 easily confused chars: 0,1,i,I,l,L,o,O

        :param trim_confused:
        :type trim_confused:
        """
        self.max_len = 6
        self.url_pre = 'https://tinyc.cn/'
        if trim_confused:
            self.alphabet = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ'
        else:
            self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.l2s = {}

    def encode(self, long_url):
        def gen():
            r = []
            for _ in range(self.max_len):
                r += self.alphabet[random.randint(0, len(self.alphabet) - 1)]

            return ''.join(r)

        key = gen()
        while key in self.l2s:
            key = gen()

        self.l2s[key] = long_url
        return self.url_pre + key

    def decode(self, short_url):
        return self.l2s[short_url[len(self.url_pre):]]


# print(IncUrl().convert('a'))
# print(ord('0'), ord('a'), ord('A'))
cod = IncUrl()

# for x in cod.alphabet:
#     print(cod.convert(x))
# print(cod.alphabet.find(x))
# v = ''
v = cod.base102alpha(3)
print(v)
n = cod.alpha2base10(v)
print(n)

ru = RandUrl(trim_confused=True)
su = ru.encode('https://www.zhihu.com/collection/94167493?page=2')
print(su)
print(ru.decode(su))
