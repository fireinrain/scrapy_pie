# -*- coding: utf-8 -*-
import scrapy
from scrapy_pie.configure import headers
from scrapy_pie.items import ScrapyPieItem


class Javbus8Spider(scrapy.Spider):
    name = 'javbus8'
    allowed_domains = ['javbus8.pw']
    start_urls = ['http://javbus8.pw/']

    page_url_set = set([start_urls[0], start_urls[0] + "page/1"])

    # pages = [start_urls[0] + "page/" + str(i) for i in range(2, 310)]

    # 使用代理请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        # ['https://www.javbus8.pw/YAL-119']
        # ['https://pics.javcdn.pw/thumb/6xcr.jpg']
        # ['友カノの寝取り顔を黙って売ってます 夢咲ひなみ']
        # ['YAL-119']
        # ['2019-01-04']
        # ['高清', '前日新種']
        # ['高清']
        film_a_tags = response.xpath('//*[@id="waterfall"]/div/a')
        for film in film_a_tags:
            film_cover_item = ScrapyPieItem()
            film_cover_item["film_url"] = film.xpath('./@href').extract_first()
            film_cover_item["film_cover_url"] = film.xpath('.//div[1]/img/@src').extract_first()
            film_cover_item["film_name"] = film.xpath('.//div[1]/img/@title').extract_first()
            film_cover_item["film_code"] = film.xpath('.//div[2]/span/date[1]/text()').extract_first()
            film_cover_item["film_pub_date"] = film.xpath('.//div[2]/span/date[2]/text()').extract_first()
            # ['高清', '前日新種']  javbus.pw 才有此数据
            # self.log(film.xpath(".//div[2]/span/div/button/text()").extract())
            # self.log(film.xpath(".//div[2]/span/div/button[@class='btn btn-xs btn-primary']/text()").extract())
            self.log(f"------------------------------{film_cover_item['film_url']}")
            yield film_cover_item

        # 截取分页
        # start_page = response.xpath("/html/body/div[6]/ul/li/a/@href").extract()
        # # 拼接为绝对url
        # pages = [self.start_urls[0] + url[1:] for url in start_page]
        # self.log(f"pages:{pages}")
        # for page_url in pages:
        #     if page_url in self.page_url_set:
        #         # 已经抓取过
        #         pass
        #     else:
        #         self.page_url_set.add(page_url)
        #         yield scrapy.Request(page_url, callback=self.parse, headers=headers)
        #
        # self.log(len(self.page_url_set))

        # 模拟解析page_url
        for index, page in enumerate([self.start_urls[0] + "page/" + str(i) for i in range(2, 313)]):
            headers["referer"] = self.start_urls[0] + "page/" + str(index + 1)
            yield scrapy.Request(page, callback=self.parse, headers=headers)
