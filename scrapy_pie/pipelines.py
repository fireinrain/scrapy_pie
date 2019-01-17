# -*- coding: utf-8 -*-
import pymysql as MySQLdb
from twisted.enterprise import adbapi

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 使用异步入库 出现 [Failure instance: Traceback: <class 'AttributeError'>: 'Connection' object has no attribute '_result'
from scrapy_pie.items import JavbusMiniItem, ShtCategoryItem, ShtItemCountItem
from scrapy_pie.utils import to_mysql_daatetime


class ScrapyPiePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
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
            db=settings['MYSQL_DBNAME'],
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
class ShtorrentPipelineSync(object):
    def __init__(self, dbpool):
        self.db = dbpool
        self.cursor = self.db.cursor()

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASS'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = MySQLdb.connect(**dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, ShtCategoryItem):
            print(item)
        elif isinstance(item, ShtItemCountItem):
            # 做判断是否要更新
            if item["total"] == 676:
                spider.logger.warn("无需更新,停止爬虫")
                spider.close(spider, "数据库为最新无需更新")
            print(item)
        else:
            return item

    def close_spider(self, spider):
        # self.db.commit()
        self.db.close()
