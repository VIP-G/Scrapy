# -*- coding: utf-8 -*-
import scrapy, json
from douyu.items import DouyuItem

'''
案例：斗鱼主播照片爬虫
http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=
'''
class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['capi.douyucdn.cn/']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']

    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0

    def parse(self, response):
        # self.log(response.text)
        data = json.loads(response.text)
        ls = data['data']
        self.log('len' + str(len(ls)))
        for i in ls:
            item = DouyuItem()
            item['name'] = i['nickname']
            item['image_url'] = i['vertical_src']
            yield item
        self.offset += 20
        next_url = self.url + str(self.offset)
        yield scrapy.Request(next_url,callback=self.parse)
