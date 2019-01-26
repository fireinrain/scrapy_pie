# -*- coding: utf-8 -*-
import pymysql as MySQLdb
import scrapy
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 使用异步入库 出现 [Failure instance: Traceback: <class 'AttributeError'>: 'Connection' object has no attribute '_result'
from scrapy_pie.items import JavbusMiniItem, ShtCategoryItem, ShtItemCountItem, ShtorrentFilmItem, ShtPageFilmListItem
from scrapy_pie.utils import to_mysql_daatetime, cut_item_url_for_unique, format_print


class ScrapyPiePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME']["scrapy_pie"],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASS'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常

    def handle_error(self, failure):
        # 处理异步插入异常
        print(failure)

    # 异步插入数据
    # 执行具体的插入语句,不需要commit操作,Twisted会自动进行
    def do_insert(self, cursor, item):
        insert_sql = "insert into film_cover(`film_name`,`film_code`,`film_url`," \
                     "`film_pub_date`,`film_cover_url`,`create_date`) values ('%s','%s','%s','%s','%s','%s')" % (
                         item['film_name'], item['film_code'], item['film_url'], item['film_pub_date'],
                         item['film_cover_url'],
                         to_mysql_daatetime()
                     )
        cursor.execute(insert_sql)

    # def process_item(self, item, spider):
    #     print(item)


# javbus同步入库
class ScrapiesPipelineSync(object):
    def __init__(self, dbpool):
        self.db = dbpool
        self.cursor = self.db.cursor()

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME']["scrapy_pie"],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASS'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = MySQLdb.connect(**dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 过滤 只对
        if isinstance(item, JavbusMiniItem):
            sql = "insert into film_cover(`film_name`,`film_code`,`film_url`,`film_pub_date`," \
                  "`film_cover_url`,`create_date`) value('%s','%s','%s','%s','%s','%s')" % (
                      item['film_name'], item['film_code'], item['film_url'], item['film_pub_date'],
                      item['film_cover_url'],
                      to_mysql_daatetime())
            self.cursor.execute(sql)
            self.db.commit()
        else:
            return item

    def close_spider(self, spider):
        # self.db.commit()
        self.db.close()


################################################

# shtorrent 同步入库
class ShtorrentDataSyncStorePipeline(object):
    def __init__(self, dbpool, crawler):
        self.db = dbpool
        self.cursor = self.db.cursor()
        self.crawler = crawler
        # 查询出已入库的作品的url
        select_url = "select parse_url from sht_films"
        self.cursor.execute(select_url)
        result = self.cursor.fetchall()
        self.url_dict = set([cut_item_url_for_unique(i["parse_url"]) for i in result])
        # print(len(self.url_dict))
        self.crawler.url_list = self.url_dict

        format_print(f"数据库中已有:{len(result)}条URL")

    @classmethod
    def from_crawler(cls, crawler):
        dbparams = dict(
            host=crawler.settings['MYSQL_HOST'],
            db=crawler.settings['MYSQL_DBNAME']["scrapy_pie"],
            user=crawler.settings['MYSQL_USER'],
            passwd=crawler.settings['MYSQL_PASS'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = MySQLdb.connect(**dbparams)
        return cls(dbpool, crawler)
        # return cls(crawler)

    @classmethod
    def from_settings(cls, settings):
        # dbparams = dict(
        #     host=settings['MYSQL_HOST'],
        #     db=settings['MYSQL_DBNAME']["scrapy_pie"],
        #     user=settings['MYSQL_USER'],
        #     passwd=settings['MYSQL_PASS'],
        #     charset='utf8',
        #     cursorclass=MySQLdb.cursors.DictCursor,
        #     use_unicode=True,
        # )
        # dbpool = MySQLdb.connect(**dbparams)
        # return cls(dbpool)
        pass

    def process_item(self, item, spider):
        if isinstance(item, ShtCategoryItem):
            pass
            # format_print(item)
        elif isinstance(item, ShtItemCountItem):
            select_sql = "select count(*) total_item from `sht_films`"
            self.cursor.execute(select_sql)
            result = self.cursor.fetchone()
            # print(result)  {'total_item': 727}
            # 做判断是否要更新
            if item["total"] == int(result['total_item']):
                format_print("无需更新,停止爬虫")
                spider.need_scrapy = False
                spider.close(spider, "数据库为最新无需更新")
            # print(item)
        elif isinstance(item, ShtPageFilmListItem):
            # 处理每页的链接
            for item_url in item["url_list"]:
                if cut_item_url_for_unique(item_url) in self.url_dict:
                    continue
                else:
                    format_print(f"正在添加：{item_url} 页面资源")
                    req = scrapy.Request(item_url, callback=spider.parse_file_page, headers=spider.header,
                                         dont_filter=True)
                    self.crawler.engine.crawl(req, spider)
                    # yield scrapy.Request(item_url, callback=spider.parse_file_page, headers=spider.header, meta={'item': item},dont_filter=True)
            # 不处理这个item了
            raise DropItem()
        elif isinstance(item, ShtorrentFilmItem):
            insert_sql = "insert into sht_films(`codes`,`code_and_title`,`film_name`,`film_stars`," \
                         "`film_format`,`film_size`,`film_code_flag`,`seed_period`,`film_preview_url`,`film_preview_url2`," \
                         "`magnent_str`,`torrent_url`,`torrent_name`,`parse_url`) value('%s','%s','%s','%s','%s','%s','%s'," \
                         "'%s','%s','%s','%s','%s','%s','%s')" % (
                             item['codes'], item['code_and_title'], item['film_name'], item['film_stars'],
                             item['film_format'], item['film_size'], item['film_code_flag'], item['seed_period'],
                             item['film_preview_url'], item['film_preview_url2'], item['magnent_str'],
                             item['torrent_url'],
                             item['torrent_name'], item['parse_url'])

            update_sql = "UPDATE `sht_films` SET `codes`='%s'," \
                         "`code_and_title`='%s',`film_name`='%s',`film_stars`='%s'," \
                         "`film_format`='%s',`film_size`='%s',`film_code_flag`='%s'," \
                         "`seed_period`='%s',`film_preview_url`='%s',`film_preview_url2`='%s'," \
                         "`magnent_str`='%s',`torrent_url`='%s',`torrent_name`='%s',`parse_url`='%s' WHERE `code_and_title`='%s'" % (
                             item['codes'], item['code_and_title'], item['film_name'], item['film_stars'],
                             item['film_format'], item['film_size'], item['film_code_flag'], item['seed_period'],
                             item['film_preview_url'], item['film_preview_url2'], item['magnent_str'],
                             item['torrent_url'],
                             item['torrent_name'], item['parse_url'], item['code_and_title'])

            select_sql = "select * from `sht_films` where `code_and_title`='%s'" % item['code_and_title']
            # 存入数据库
            # https://sehuatang.org/thread-26748-1-25.html 数据有重复 IPX-150
            self.cursor.execute(select_sql)
            ret = self.cursor.fetchone()
            if ret:
                self.cursor.execute(update_sql)
                self.db.commit()
            else:
                self.cursor.execute(insert_sql)
                self.db.commit()

        else:
            pass
        return item

    def close_spider(self, spider):
        # self.db.commit()
        self.db.close()
