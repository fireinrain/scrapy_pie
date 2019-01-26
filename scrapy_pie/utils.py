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
from random import choice

UserAgent = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
    'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
]

# 主站访问headers
sht_headers = {
    'Host': 'www.54sadsad.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': choice(UserAgent),
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'}

# 样品图下载headers
sht_img_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,zh;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,ja;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': choice(UserAgent)
}


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
            multi = int((11 / chinese_chars_length) * 0.688)
            print(strs, (int(max_str * 1.62) - not_zh_size - 1 * multi) * " ", table_end_template)

        print("-" * int(max_str * 1.62))


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    for c in uchar:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


def get_sht_img_header():
    """
    获取sht img header
    :return:
    """
    return sht_img_headers


if __name__ == '__main__':
    print(to_mysql_daatetime())
    test_str = "Your spider is running now!"
    format_print(f"{test_str}")
