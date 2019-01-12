# -*- coding: utf-8 -*-
import scrapy

from scrapy_pie.configure import headers


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def start_requests(self):
        # for url in self.start_urls:
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=headers)

    def parse(self, response):
        pass
