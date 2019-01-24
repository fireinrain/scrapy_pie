# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# javbus
class JavbusMiniItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 影片名字
    film_name = scrapy.Field()
    # 番号
    film_code = scrapy.Field()
    # 影片访问连接
    film_url = scrapy.Field()
    # 影片发行时间
    film_pub_date = scrapy.Field()
    # 影片mini封面
    film_cover_url = scrapy.Field()


# shtorrent
# 1 类目item
class ShtCategoryItem(scrapy.Item):
    # 类别名字
    category_name = scrapy.Field()
    # 类别链接
    category_url = scrapy.Field()


class ShtItemCountItem(scrapy.Item):
    # 有码
    code_kind = scrapy.Field()
    code_count = scrapy.Field()
    # 无码
    nocode_kind = scrapy.Field()
    nocode_count = scrapy.Field()
    # 总数
    total = scrapy.Field()


class ShtorrentFilm(scrapy.Item):
    # 链接
    parse_url = scrapy.Field()
    # 番号 作品名
    code_and_title = scrapy.Field()
    # 番号
    codes = scrapy.Field()
    # 名称
    film_name = scrapy.Field()
    # 演员
    film_stars = scrapy.Field()
    # 格式
    film_format = scrapy.Field()
    # 大小
    film_size = scrapy.Field()
    # 是否有码
    film_code_flag = scrapy.Field()
    # 种子期限
    seed_period = scrapy.Field()
    # 封面链接
    film_preview_url = scrapy.Field()
    #  short view
    film_preview_url2 = scrapy.Field()
    # 磁力链接
    magnent_str = scrapy.Field()
    # 种子链接
    torrent_url = scrapy.Field()
    # 种子名称
    torrent_name = scrapy.Field()
