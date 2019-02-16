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
from .db_utils import cursor


def compute_total_size():
    """
    计算数据库中的所有大小
    :return:
    """
    sql = "select `file_size` from info"
    result = cursor.execute(sql)
    all_size = [float(i[0][:-2]) for i in result]
    # 总大小：3043.4000000000037GB
    # 平均大小：5.57GB
    # 数量：

    statics = f"""
    总大小：{sum(all_size)}GB
    平均大小：{float(sum(all_size) / len(all_size))}GB
    数量：{len(all_size)}
    """
    print(statics)


def compute_star_count():
    """ 不是很准确
    计算有多少演员
    :return:
    """
    sql = "select `av_stars` from info"
    result = cursor.execute(sql)
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
