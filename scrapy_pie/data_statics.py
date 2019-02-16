#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 数据统计
@software: pycharm
@file: data_statics.py
@time: 2018/12/30 13:38
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from scrapy_pie.db_utils import cursor


def compute_total_size():
    """
    计算数据库中的所有大小
    :return:
    """
    sql = "select `film_size` from sht_films"
    cursor.execute(sql)
    # 这里和sqlite不一样
    # sqlite 执行excute后 可以直接获取结果集合
    # 但是mysql 需要使用cursor.fetchall()
    result = cursor.fetchall()
    count = len(result)
    # print(result)
    all_size = 0
    for i in result:
        if 'GB' in i[0]:
            # print(i)
            value = i[0][:-2]
            all_size+=float(value)
        else:
            value = float(i[0].split('.')[0])
            all_size+=value
    # all_size = [float(i[0][:-2]) for i in result]
    # # 总大小：3043.4000000000037GB
    # # 平均大小：5.57GB
    # # 数量：
    #
    statics = f"""
    总大小：{all_size}GB
    平均大小：{all_size / count}GB
    数量：{count}
    """
    print(statics)


def compute_star_count():
    """ 不是很准确
    计算有多少演员
    :return:
    """
    sql = "select `film_stars` from sht_films"
    cursor.execute(sql)
    result = cursor.fetchall()
    stars_collection = [i[0] for i in result]
    # print(stars_collection)

    info_dict = dict()
    for i in stars_collection:
        if i not in info_dict.keys():
            info_dict[i] = 1
        else:
            info_dict[i] += 1
    # print(info_dict)

    info_list = [i for i in info_dict.items()]
    statics = sorted(info_list, key=lambda i: i[1], reverse=True)
    for i in statics:
        bar = "-----"
        bar = bar* i[1]
        print(bar+">>"+str(i))


if __name__ == '__main__':
    compute_total_size()
    print("-------------------------统计分析----------------------------")
    compute_star_count()
