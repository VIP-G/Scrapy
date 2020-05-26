# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings


class ImagewordPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 图片下载完成触发方法
        # 对图片改名
        print('result', results)
        # if results[0][0] == True:
        #     # 图片原路径
        #     s_path = self.IMAGES_STORE + '/' + results[0][1]['path']
        #     # 目标路径
        #     d_path = self.IMAGES_STORE + '/' + item['name'] + '.jpg'
        #     os.rename(s_path, d_path)
        #     item['image_Path'] = d_path
        #     return item
