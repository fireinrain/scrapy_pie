#!/usr/bin/env python
# encoding: utf-8
"""
@desc:工具方法
@software: pycharm
@file: utils.py
@time: 2019/1/12 13:27
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import datetime


def to_mysql_daatetime():
    """
    返回当前时间字符串
    :return:
    """
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def cut_item_url_for_unique(url):
    """
    将 'http://www.54sadsad.com/thread-54251-1-7.html'
    截取为 ‘http://www.54sadsad.com/thread-54251-1'
    :param url:
    :return:
    """
    index = url.rindex("-")
    return url[:index]


if __name__ == '__main__':
    print(to_mysql_daatetime())
