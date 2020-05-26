# -*- coding: utf-8 -*-
import scrapy
from imageword.items import ImagewordItem

'''

图行天下图片爬虫
http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5
爬取海报图片保存到 images 目录下
'''


class ImgwordSpider(scrapy.Spider):
    name = 'imgword'
    allowed_domains = ['so.photophoto.cn']
    start_urls = ['http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5']

    url = 'http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5/1-0-0-0-0-2-0-2.html'

    def parse(self, response):
        ls = response.xpath('//ul[@id="list"]/li')
        self.log('len' + str(len(ls)))
        for i in ls:
            name = i.xpath('.//img/@alt').extract()[0]
            image_url = 'http:' + i.xpath('.//img/@src').extract()[0]
            self.log('标题:' + name)
            self.log('连接:' + image_url)
            item = ImagewordItem()
            item['name'] = name
            item['image_url'] = image_url
            yield item
        next_btn = response.xpath('//div[@id="page"]/a[@class="pagenext"]/@href').extract()[0]
        base_url = 'http://so.photophoto.cn'
        if len(next_btn):
            next_page_url = base_url + next_btn
            self.log('next_page_url:' + next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
