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
        # 出去栏目
        films_item1 = response.xpath('//div[contains(@id,"category_166")]')
        films_item2 = response.xpath('//div[contains(@id,"category_55")]')

        for cat_url in films_item1:
            tag_url = cat_url.xpath('.//*/tr/td/a/@href').extract()
            for cat in tag_url:
                print(cat)

