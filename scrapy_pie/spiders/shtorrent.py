# -*- coding: utf-8 -*-
import scrapy

# 对 https://www.sehuatang.org/forum-103-1.html
# 该网页的中文字幕种子下载，并将相关数据保存到数据库中
# 默认请求走了本地的shadowsocks代理
from scrapy_pie.configure import sht_headers


class ShtorrentSpider(scrapy.Spider):
    name = 'shtorrent'
    allowed_domains = ['sehuatang.org']
    start_urls = ['http://sehuatang.org/']

    def __init__(self):
        self.header = sht_headers

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.header)

    def parse(self, response):
        print(response)
