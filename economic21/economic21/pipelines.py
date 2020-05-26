# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class Economic21PipelineMongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['db_21']
        self.conn = self.db.econo_21

    def process_item(self, item, spider):
        self.conn.insert_one(
            {'title': item['title'],
             'date': item['date'],
             'source': item['source'],
             'content': item['content']
             }
        )

        return item
    def close_spider(self, spider):
        '''
        关闭时会触发该方法
        :param spider:
        :return:
        '''
        self.conn.close()
        self.db.close()