#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: db_utils.py
@time: 2018/12/28 22:28
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import pymysql

from scrapy_pie.settings import MYSQL_DBNAME, MYSQL_HOST, MYSQL_PASS, MYSQL_USER
conn = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASS,MYSQL_DBNAME["scrapy_pie"])
cursor = conn.cursor()


def init_db():
    """
    初始化db
    :return:
    """

    table_films_creat_sql = "create table if not exists sht_films(" \
                            "`id` integer primary key AUTO_INCREMENT,`codes` varchar(50) ," \
                            "`code_and_title` varchar(255),`film_name` varchar(255)," \
                            "`film_stars` varchar(100),`film_format` varchar(20)," \
                            "`film_size` varchar(10),`film_code_flag` varchar(10)," \
                            "`seed_period` varchar(20),`film_preview_url` varchar(255)," \
                            "`film_preview_url2` varchar(255),`magnent_str` varchar(255)," \
                            "`torrent_url` varchar(255),`torrent_name` varchar(80)," \
                            "`parse_url`varchar(255) )"


    cursor.execute(table_films_creat_sql)


# print(f"resource_table 创建成功------！")
# insert into url_set( `url`,`flag`) select item_url,1 from films as urls  从一张表中取出数据然后插入到另一张表中
if __name__ == '__main__':
    init_db()