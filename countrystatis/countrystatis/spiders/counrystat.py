# -*- coding: utf-8 -*-
import datetime

import scrapy
from countrystatis.items import CountrystatisItem

class CounrystatSpider(scrapy.Spider):
    name = 'counrystat'
    allowed_domains = ['www.stats.gov.cn/']
    start_urls = ['http://www.stats.gov.cn/tjsj/zxfb/index.html']

    def parse(self, response):
        ls = response.xpath('//ul[@class="center_list_contlist"]/li/a')
        for i in ls:
            detail_url = i.xpath('./@href').extract()[0]
            if detail_url.startswith('/'):
                detail_url = 'http://www.stats.gov.cn' + detail_url

                # self.log('详情连接：' + detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail)
            else:
                detail_url = detail_url.replace('./', 'http://www.stats.gov.cn/tjsj/zxfb/')
                # self.log('详情连接：' + detail_url)
                yield scrapy.Request(detail_url, callback=self.parse_detail)
        next_url = response.xpath('//a[@id="pagenav_1"]/@href').extract()[0]
        base_next_url = 'http://www.stats.gov.cn/tjsj/zxfb/'
        if next_url:
            next_url = base_next_url + next_url
            self.log('下页连接：' + next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, res):
        title=res.xpath('//h2[@class="xilan_tit"]/text()').extract()[0]
        self.log('标题：' + title)
        date=res.xpath('//font[@class="xilan_titf"]/font//text()').extract()
        self.log(date)
        # self.log('时间：' + date)
