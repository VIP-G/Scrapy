# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs
import pymysql
from scrapy.exporters import JsonItemExporter


class JobspiderPipeline(object):

    def process_item(self, item, spider):
        return item
