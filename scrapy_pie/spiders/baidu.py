# -*- coding: utf-8 -*-
import scrapy

from scrapy_pie.configure import sht_headers


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    test_page_url = "https://www.sehuatang.org/thread-35837-1-22.html"
    test_page_url2 = "https://www.sehuatang.org/thread-74972-1-1.html"

    def __init__(self):
        self.header = sht_headers

    def start_requests(self):
        yield scrapy.Request(self.test_page_url2, callback=self.parse, headers=self.header)

    # 解析测试专用
    def parse(self, response):
        """
        格式：
        # DVAJ-355 女友不在家的三天里和她的好朋友做爱不停
        #
        # 【影片名称】：女友不在家的三天里和她的好朋友做爱不停
        #
        # 【出演女优】：里梨夏 富田優衣
        #
        # 【影片格式】：MP4
        #
        # 【影片大小】：5.46GB
        #
        # 【是否有码】：有码
        #
        # 【种子期限】：5种或健康度1000
        # ['https://www.sehuatuchuang.com/tupian/forum/201901/19/115021cl0gek57rcrx7oa5.jpg']
        # magnet:?xt=urn:btih:9FBAEB5A0CFAB8E379FCACE5FA05D209E4C813F2
        # forum.php?mod=attachment&aid=NzAyNDF8ODM0NzExMmJ8MTU0NzkyMzI1OHwwfDc0OTcy
        # [7sht.me]DVAJ-355-C.torrent
        :param response:
        :return:
        """
        # 标题和番号
        code_and_title = response.xpath('//*[@id="thread_subject"]/text()').extract_first()
        # 片名
        film_name = response.xpath('//*[@class="t_f"]/text()[1]').extract_first()  # .split("：")[1].strip()
        # 演员
        film_stars = response.xpath('//*[@class="t_f"]/text()[2]').extract_first()
        # 影片格式
        film_format = response.xpath('//*[@class="t_f"]/text()[3]').extract_first()
        # 影片大小
        film_size = response.xpath('//*[@class="t_f"]/text()[4]').extract_first()
        # 是否有码
        film_code_flag = response.xpath('//*[@class="t_f"]/text()[5]').extract_first()
        # 种子期限
        seed_period = response.xpath('//*[@class="t_f"]/text()[6]').extract_first()
        # 影片预览
        # film_preview = response.xpath('//*[@class="t_f"]/text()[7]').extract_first()
        # 影片介绍
        # film_introduction = response.xpath('//*[@class="t_f"]/text()[8]').extract_first()

        # '//*[@id="aimg_20280"]'
        film_preview_url = response.xpath('//*[@class="t_f"]/img/@file').extract_first()
        film_preview_url2 = response.xpath('//*[@class="t_f"]/ignore_js_op/img[contains(@id,"aimg_")]/@file').extract_first()

        magnent_str = response.xpath('//*[contains(@id,"code_")]/ol/li/text()').extract_first()

        # '//*[@id="pid106962"]/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[2]/ignore_js_op'
        # '//*[@id="pid106962"]/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[2]/ignore_js_op/dl/dd/p[1]'
        torrent_url = response.xpath('//*[@class="attnm"]/a/@href').extract_first()
        torrent_name = response.xpath('//*[@class="attnm"]/a/text()').extract_first()
        print(code_and_title)
        print(film_name)
        print(film_stars)
        print(film_format)
        print(film_size)
        print(film_code_flag)
        print(seed_period)
        print(film_preview_url)
        print(film_preview_url2)
        print(magnent_str)
        print(torrent_url)
        print(torrent_name)
