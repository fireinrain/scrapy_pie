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

# 创建sqlite3 数据库 保存item信息
import os
import pymysql

from .settings import MYSQL_DBNAME, MYSQL_HOST, MYSQL_PASS, MYSQL_USER

conn = pymysql.connect()
cursor = conn.cursor()


def init_db():
    """
    初始化db
    :return:
    """

    table_films_creat_sql = "create table if not exists films(" \
                            "`id` integer primary key autoincrement,`code` varchar(30) ," \
                            "`filename` varchar(30),`item_url` varchar(80))"

    table_info_create_sql = "create table if not exists info(" \
                            "`id` integer primary key autoincrement,`films_id` int ," \
                            "`film_name` varchar(30) ,`av_stars` varchar(30), " \
                            "`file_format` varchar(30),`file_size` varchar(30)," \
                            "`mosaic` int(1),`seed_info` varchar(30))"

    table_resource_create_sql = "create table if not exists resource(" \
                                "`id` integer primary key autoincrement,`info_id` int ," \
                                "`sample_img` varchar(100) ,`sample_img2` varchar(100), " \
                                "`magnent_code` varchar(80),`torrent_url` varchar(120)," \
                                "`torrent_name` varchar(30))"

    table_url_set_create_sql = "create table if not exists url_set(" \
                               "`id` integer primary key autoincrement,`url` varchar(80),`flag` int(1))"

    cursor.execute(table_films_creat_sql)
    # print(f"films_table 创建成功------!")
    cursor.execute(table_info_create_sql)
    # print(f"info_table 创建成功------！")
    cursor.execute(table_resource_create_sql)
    # print(f"url_set_table 创建成功------！")
    cursor.execute(table_url_set_create_sql)

# print(f"resource_table 创建成功------！")
# insert into url_set( `url`,`flag`) select item_url,1 from films as urls  从一张表中取出数据然后插入到另一张表中
