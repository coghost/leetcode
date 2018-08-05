# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '25/09/2017 11:13 AM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys
from functools import wraps

app_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_root)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

import linecache

counter = 0
enable_trace = True


def trace(do=enable_trace, show_detail=False):
    """ 追踪程序运行情况总次数, 如果show_detail == True, 则打印每一步

    :param do:
    :type do:
    :param show_detail:
    :type show_detail:
    :return:
    :rtype:
    """

    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        global counter
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno

            bname = os.path.basename(filename)
            if show_detail:
                print("{}({} - {}): {}".format(bname,
                                               counter,
                                               lineno,
                                               linecache.getline(filename, lineno)), end=',')
            counter += 1
        return localtrace

    if not hasattr(do, '__call__'):

        def dec(fn):
            @wraps(fn)
            def _f(*args, **kwargs):
                global counter
                if not do:
                    return fn(*args, **kwargs)
                sys.settrace(globaltrace)
                counter = 0
                result = fn(*args, **kwargs)
                sys.settrace(None)
                if not show_detail:
                    print('[{}] running {} times'.format(fn.__name__, counter))
                return result

            return _f

        return dec
