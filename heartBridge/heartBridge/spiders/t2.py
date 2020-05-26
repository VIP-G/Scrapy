# -*- coding: utf-8 -*-
import scrapy
from heartBridge.items import HeartbridgeItem


class T2Spider(scrapy.Spider):
    name = 't2'
    allowed_domains = ['zynews.cn']
    start_urls = ['https://xtq.zynews.cn/wzpostlist.php?mod=list']

    def parse(self, response):

        ls = response.xpath('//div[@class="bm_c"]/table/tbody/tr')
        self.log('len:' + str(len(ls)))
        base_url = 'https://xtq.zynews.cn/'
        for i in ls:
            item = HeartbridgeItem()
            item['title'] = i.xpath('.//th[@class="new"]/a/text()').extract()[0].strip()
            item['url'] = base_url + i.xpath('.//th[@class="new"]/a/@href').extract()[0]
            item['author'] = i.xpath('.//td[@class="by"]/cite/a/text()').extract()[0]
            item['date'] = i.xpath('.//td[@class="by"]/em/span/text()').extract()[0]
            req = scrapy.Request(item['url'], callback=self.parse_detail, dont_filter=True)
            req.meta['item'] = item
            yield req
        next_btn = response.xpath('//a[@class="nxt"]')
        if len(next_btn) > 0:
            next_page_url = base_url + next_btn[0].xpath('./@href').extract()[0]
            self.log('next_page_url:' + next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, res):
        item = res.meta['item']
        content = res.xpath('//td[@class="t_f"]/text()').extract()
        content = ''.join(content)
        self.log('content:' + content)
        item['content'] = content
        yield item
