# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings


class ShoesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)
