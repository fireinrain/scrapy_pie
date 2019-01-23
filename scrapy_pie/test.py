#!/usr/bin/env python
# encoding: utf-8
"""
@desc:用来测试一些api的用法
@software: pycharm
@file: test.py
@time: 2019/1/12 1:18
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import pymysql
from scrapy import Selector


def test_selector():
    html_strs = ""
    with open('./index.html', 'r+', encoding='utf8') as file:
        html_strs = file.read()
        # print(html_strs)
        sel = Selector(text=html_strs, type="html")

        link = sel.xpath('//*[@id="waterfall"]/div[12]/a').extract_first()
        print(link)


def test_range():
    rangs = [i for i in range(2, 313)]
    print(rangs)


def test_encode():
    s = '濃厚ベロチューしながらスローオイル手こきでち○ぽ焦らされ続ける。その2'
    print(s.encode(encoding='gbk').decode(encoding='gbk'))
    print(s.encode(encoding='utf8').decode())


def test_config():
    from scrapy_pie.configure import headers
    print(headers)


def test_db():
    pymysql.connect()


def test_code():
    torrent_name = "[7sht.me]MIDE-458-C.torrent"
    print(torrent_name.split("]")[1].split(".")[0][:-2])


def test_error_film_name():
    html_strs = ""
    with open('./sampledata/sht/error_film.html', 'r+', encoding='utf8') as file:
        html_strs = file.read()
        # print(html_strs)
        sel = Selector(text=html_strs, type="html")
        # '//*[@id="postmessage_271824"]/text()[1]'
        # ‘//div[contains(@id,”test”) and contains(@id,”title”)]’
        link = sel.xpath('//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()[3]').extract()
        print(link)


if __name__ == '__main__':
    # test_selector()
    # test_range()
    # test_encode()
    # test_config()
    # test_code()
    test_error_film_name()