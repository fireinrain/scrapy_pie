# -*- coding: utf-8 -*-
import scrapy

from scrapy_pie.configure import headers


class ThztorrentSpider(scrapy.Spider):
    name = 'thztorrent'
    allowed_domains = ['thzvv.net']
    start_urls = ['http://thzvv.net/', ]

    # 为每个爬虫指定不同的pipeline
    custom_settings = {
        'ITEM_PIPELINES': {

        }
    }

    def start_requests(self):
        # for url in self.start_urls:
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=headers)

    def parse(self, response):
        pass
