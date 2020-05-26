# -*- coding: utf-8 -*-
import scrapy, re
from shoes.items import ShoesItem

'''
鞋天地图片爬虫
http://www.xietd.com/
'''


class ShoesimgSpider(scrapy.Spider):
    name = 'shoesimg'
    allowed_domains = ['xietd.com']
    start_urls = ['http://www.xietd.com/portal.php?&page=1#tab_anchor']

    def parse(self, response):
        ls = response.xpath('//div[@class="work-list-box"]/div')
        self.log('len' + str(len(ls)))
        for i in ls:
            detail_url = i.xpath('.//div[@class="card-img"]/a/@href').extract()[0]
            self.log('detail_url:' + detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)
        next_btn = response.xpath('//div[@class="pg"]//a[text()="下一页"]')
        if len(next_btn) > 0:
            next_page_url = next_btn[0].xpath('./@href').extract()[0]

            self.log('next_page_url:' + next_page_url)
            # 把请求对象发送给schedule，放入请求等待队列
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        item = ShoesItem()
        base_url = 'http://www.xietd.com/'
        name = response.xpath('//div[@class="details-contitle-box"]/h2/text()').extract()[0]
        name = name.strip().split(' ')[0]
        item['name'] = name
        self.log('name:' + name)
        img_url = response.xpath('//div[@class="aimg"]/img/@zoomfile').extract()
        if len(img_url) > 0:
            for x in img_url:
                img_url = base_url + x
                self.log('img_url:' + img_url)

                item['img_url'] = img_url
                yield item
