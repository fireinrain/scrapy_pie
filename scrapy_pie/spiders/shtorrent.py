# -*- coding: utf-8 -*-
import scrapy

# 对 https://www.sehuatang.org/forum-103-1.html
# 该网页的中文字幕种子下载，并将相关数据保存到数据库中
# 默认请求走了本地的shadowsocks代理
from scrapy_pie.configure import sht_headers


class ShtorrentSpider(scrapy.Spider):
    name = 'shtorrent'
    allowed_domains = ['sehuatang.org']
    # 有时你填写http也可以返回正确的response
    # 但是最好写成和浏览器访问的一支
    # 要不然会报错：https://github.com/scrapy/scrapy/issues/3103
    start_urls = ['https://sehuatang.org/']

    def __init__(self):
        self.header = sht_headers

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.header)

    def parse(self, response):
        print(response)
