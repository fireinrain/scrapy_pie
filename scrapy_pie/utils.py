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


def format_print(message):
    """
    格式化打印消息
    :param message:
    :return:
    """
    size = len(str(message))
    print("-" * int(size*3.5))
    print(f">>>>>>>>{message}")
    print("-"*int(size*3.5))


def table_formate_print(item):
    """
    按照表格打印对象中的属性和值
    :param item:
    :return:
    """
    pass


if __name__ == '__main__':
    print(to_mysql_daatetime())
    test_str = "Your spider is running now!"
    format_print(f"{test_str}")
