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
import math

import pymysql
from scrapy import Selector

from scrapy_pie.items import ShtorrentFilmItem
from scrapy_pie.utils import table_formate_print, is_chinese


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
    con = pymysql.connect(host="192.168.11.117",
                          user="root",
                          passwd="sunriseme1994",
                          database="scrapy_pie_db")
    cursor = con.cursor()
    item = {'code_and_title': 'PGD-677 淫荡痴女教师小川阿佐美[高清中文字幕]',
            'codes': 'pgd-677',
            'film_code_flag': '有码',
            'film_format': 'MP4',
            'film_name': '淫荡痴女教师小川阿佐美',
            'film_preview_url': 'https://jp.netcdn.space/digital/video/pgd00677/pgd00677pl.jpg',
            'film_preview_url2': 'https://www.sehuatuchuang.com/tupian/forum/201812/20/094141qnptpbpcpb66mm6o.jpg',
            'film_size': '6.87GB',
            'film_stars': '小川あさ美',
            'magnent_str': 'magnet:?xt=urn:btih:46A6CD10F2BA4B2B0425503DE244EFF1C5277B04',
            'seed_period': '5种或健康度1000',
            'torrent_name': '[7sht.me]pgd-677-C.torrent',
            'torrent_url': 'https://sehuatang.org/forum.php?mod=attachment&aid=NjIwNjB8NzQwMDRhNjV8MTU0ODI2Mzk0MXwwfDYyNTA3'}

    insert_sql = "insert into sht_films(`codes`,`code_and_title`,`film_name`,`film_stars`," \
                 "`film_format`,`film_size`,`film_code_flag`,`seed_period`,`film_preview_url`,`film_preview_url2`," \
                 "`magnent_str`,`torrent_url`,`torrent_name`) value('%s','%s','%s','%s','%s','%s','%s'," \
                 "'%s','%s','%s','%s','%s','%s')" % (
                     item['codes'], item['code_and_title'], item['film_name'], item['film_stars'],
                     item['film_format'], item['film_size'], item['film_code_flag'], item['seed_period'],
                     item['film_preview_url'], item['film_preview_url2'], item['magnent_str'],
                     item['torrent_url'],
                     item['torrent_name'])

    update_sql = "UPDATE `sht_films` SET `codes`='%s'," \
                 "`code_and_title`='%s',`film_name`='%s',`film_stars`='%s'," \
                 "`film_format`='%s',`film_size`='%s',`film_code_flag`='%s'," \
                 "`seed_period`='%s',`film_preview_url`='%s',`film_preview_url2`='%s'," \
                 "`magnent_str`='%s',`torrent_url`='%s',`torrent_name`='%s' WHERE `codes`='%s'" % (
                     item['codes'], item['code_and_title'], item['film_name'], item['film_stars'],
                     item['film_format'], item['film_size'], item['film_code_flag'], item['seed_period'],
                     item['film_preview_url'], item['film_preview_url2'], item['magnent_str'],
                     item['torrent_url'],
                     item['torrent_name'], item['codes'])

    cursor.execute(update_sql)
    con.commit()
    print(insert_sql)


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
        # link = sel.xpath('//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()[3]').extract()
        # print(link)
        film_code_flag = sel.xpath(
            '//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()').extract()
        print(film_code_flag)


def test_error_film_name2():
    html_strs = ""
    with open('./sampledata/sht/error_film2.html', 'r+', encoding='utf8') as file:
        html_strs = file.read()
        # print(html_strs)
        sel = Selector(text=html_strs, type="html")
        # '//*[@id="postmessage_271824"]/text()[1]'
        # ‘//div[contains(@id,”test”) and contains(@id,”title”)]’
        link = sel.xpath('//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()[3]').extract()
        film_name = ""
        try:
            film_name = sel.xpath('//*[@class="t_f"]/text()[1]').extract_first().split("：")[1].strip()
        except Exception as e:
            print("dddd")
        # //*[@id="postmessage_266574"]/text()[1]
        kk = sel.xpath('//*[@class="t_f"]/text()[1]').extract_first()

        # //*[@id="postmessage_266574"]/text()[6]
        film_code_flag = sel.xpath(
            '//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()').extract()

        size = sel.xpath(('//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/font/font/text()')).extract()
        film_size = sel.xpath(
            '//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()[9]').extract_first().split(
            "：")[
            1].strip()
        # //*[@id="postmessage_266574"]/text()[6]
        # film_code_flag = sel.xpath(
        #     '//td[contains(@class,"t_f") and contains(@id,"postmessage_")]/text()[7]').extract_first().split(
        #     "：")[
        #     1].strip()
        print(link)
        # print(film_name)
        print(kk)
        print(film_code_flag)
        print(size)
        print(film_size)
        # print(film_code_flag)


def test_error_film_name3():
    html_strs = ""
    with open('./sampledata/sht/error_film3.html', 'r+', encoding='utf8') as file:
        html_strs = file.read()
        # print(html_strs)
        sel = Selector(text=html_strs, type="html")
        # '//*[@id="postmessage_271824"]/text()[1]'
        # ‘//div[contains(@id,”test”) and contains(@id,”title”)]’
        # //*[@id="postmessage_296144"]/font[1]
        film_name = ""
        try:
            film_name = sel.xpath('//*[@class="t_f"]/font[1]/text()').extract_first().split("：")[1].strip()
        except Exception as e:
            print("dddd")

        print(film_name)
        # print(film_code_flag)

def test_error_film_name4():
    html_strs = ""
    with open('./sampledata/sht/error_film4.html', 'r+', encoding='utf8') as file:
        html_strs = file.read()
        # print(html_strs)
        sel = Selector(text=html_strs, type="html")
        # '//*[@id="postmessage_271824"]/text()[1]'
        # ‘//div[contains(@id,”test”) and contains(@id,”title”)]’
        # //*[@id="postmessage_296144"]/font[1]
        film_name = ""
        try:
            film_name = sel.xpath('////td[contains(@class,"t_f") and contains(@id,"postmessage_")]/font/font/text()').extract_first().split("：")[1].strip()
        except Exception as e:
            print("dddd")

        print(film_name)
        # print(film_code_flag)

def test_extract_codes():
    a = "[168x.me]ABP-036.torrent"
    b = "[7sht.me]MIDE-458-C.torrent"
    start = a.index("]")
    end = a.rindex(".")

    start1 = b.index("]")
    end1 = b.rindex(".")
    print(start, "-", end)
    print(start1, "-", end1)
    print("-".join(a[start + 1:end].split("-")[:2]))
    print("-".join(b[start + 1:end1].split("-")[:2]))


def test_get_code():
    a = "abp-566-C.torrent"
    print(a.split(".")[0][:-2])


def test_table_formate_print():
    shtorrentfilmitem = ShtorrentFilmItem()

    shtorrentfilmitem["parse_url"] = "www.baidu.com"
    shtorrentfilmitem["film_code_flag"] = "有码"
    shtorrentfilmitem["film_size"] = "5GB"
    shtorrentfilmitem["film_name"] = "经典武侠大戏陆小凤传奇经典武侠大戏陆小凤传奇"
    shtorrentfilmitem["torrent_name"] = "xxx.torrent"
    shtorrentfilmitem["film_stars"] = "贾静雯"
    shtorrentfilmitem["torrent_url"] = "abc.torrent"
    shtorrentfilmitem["magnent_str"] = "madsds:xxxxxxxsdsdassdsdsasdsadasfasdasdsasdasda"
    shtorrentfilmitem["film_preview_url"] = "http://sdsasdasd.sdasdasdas..dasdasdsadsasdsa.d.as.dasdasdasdas"
    shtorrentfilmitem["film_preview_url2"] = "http://sdswrerfdsfdsfdfsd.vom/a.jpg"
    shtorrentfilmitem["seed_period"] = "200"
    shtorrentfilmitem["film_format"] = "mp4"
    shtorrentfilmitem["code_and_title"] = "abc-123 经典武侠大戏陆小凤传奇"
    shtorrentfilmitem["codes"] = "abc-123"
    for i in shtorrentfilmitem.fields:
        print(shtorrentfilmitem[str(i)])
    print(shtorrentfilmitem)
    print(1 / 0.618)
    print("---------------------------------------------------------")
    max_str = max([len(str(shtorrentfilmitem[str(i)])) for i in shtorrentfilmitem.fields])
    print(max_str)
    header_template = "||||||||"
    print("-" * int(max_str * 1.62))
    for i in shtorrentfilmitem.fields:
        strs = f"{header_template} {i}:  {shtorrentfilmitem[str(i)]}"
        chinese_chars = [i for char in strs if is_chinese(char)]
        size = len(strs)
        not_zh_size = size - len(chinese_chars)
        chinese_chars_len = len(chinese_chars) * math.ceil(11 / 6)
        not_zh_size = not_zh_size + chinese_chars_len

        if not chinese_chars:
            print(strs, (int(max_str * 1.62) - (not_zh_size + 3)) * " ", "|")
            print(f"**{chinese_chars}")
        else:
            print(strs, (int(max_str * 1.62) - not_zh_size+1) * " ", "|")

        print("-" * int(max_str * 1.62))
    print(len("经典武侠大戏陆小凤传奇"))
    print("经级级")
    print("-" * 6)
    print(math.ceil(11 / 6))

    table_formate_print(shtorrentfilmitem, head_template="*",end_template=None)


if __name__ == '__main__':
    # test_selector()
    # test_range()
    # test_encode()
    # test_config()
    # test_code()
    # test_error_film_name()
    # test_db()
    # test_extract_codes()
    # test_get_code()
    # test_error_film_name2()
    # test_table_formate_print()
    # test_error_film_name3()
    test_error_film_name4()
