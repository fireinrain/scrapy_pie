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
import math


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
    print("-" * int(size * 3.5))
    print(f">>>>>>>>{message}")
    print("-" * int(size * 3.5))


def table_formate_print(item, head_template=None, end_template=None):
    """
    按照表格打印对象中的属性和值
    :param item:
    :param table_head_template:
    :return:
    """
    if head_template is None:
        table_head_template = "|" * 8
    else:
        table_head_template = head_template * 8
    if end_template is None:
        table_end_template = "|"
    else:
        table_end_template = end_template

    max_str = max([len(str(item[str(i)])) for i in item.fields])
    print(max_str)
    print("-" * int(max_str * 1.62))
    for i in item.fields:
        strs = f"{table_head_template} {i}:  {item[str(i)]}"
        chinese_chars = [i for char in strs if is_chinese(char)]
        size = len(strs)
        not_zh_size = size - len(chinese_chars)
        # 中文字符的长度用len()算也是一个字符，所以不好计较
        # 计算的时候会有误差，这里只是算一个中文字符的宽度大概是多少个
        # ascii的几倍，不够完美
        chinese_chars_len = len(chinese_chars) * math.ceil(11 / 6) - 1
        not_zh_size = not_zh_size + chinese_chars_len
        if not chinese_chars:
            print(strs, (int(max_str * 1.62) - (not_zh_size + 3)) * " ", table_end_template)
            # print(f"**{chinese_chars}")
        else:
            chinese_chars_length = len(chinese_chars)
            # 长度参数补偿
            multi = int((11/chinese_chars_length)*0.688)
            print(strs, (int(max_str * 1.62) - not_zh_size - 1*multi) * " ", table_end_template)

        print("-" * int(max_str * 1.62))


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    for c in uchar:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


if __name__ == '__main__':
    print(to_mysql_daatetime())
    test_str = "Your spider is running now!"
    format_print(f"{test_str}")
