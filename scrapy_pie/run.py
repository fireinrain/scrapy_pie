#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 运行入口
@software: pycharm
@file: run.py
@time: 2019/1/11 21:35
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute(['scrapy', 'crawl', 'javbus8'])
    # cmdline.execute(['scrapy', 'crawl', 'shtorrent'])

    cmdline.execute(['scrapy', 'crawl', 'baidu'])
    # cmdline.execute(['scrapy', 'crawl', 'google'])

