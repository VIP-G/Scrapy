# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from heartBridge.items import HeartbridgeItem

'''
案例：心通桥分布式爬虫
https://xtq.zynews.cn/wzpostlist.php?mod=list
爬去投诉帖子的标题，链接，内容，投诉者，投诉时间
存储到mysql数据库
'''
class Heartb2Spider(RedisSpider):
    name = 'heartB2'
    # allowed_domains = ['zynews.cn']
    # start_urls = ['http://zynews.cn/']
    redis_key = 'heartB2:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Heartb2Spider, self).__init__(*args, **kwargs)

    def parse(self, response):
        ls = response.xpath('//div[@class="bm_c"]//tbody/tr/th/a/@href').extract()
        self.log('len:' + str(len(ls)))
        base_url = 'https://xtq.zynews.cn/'
        for i in ls:
            detail_url = base_url + i
            self.log('detail_url:' + detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail, dont_filter=True)
        next_btn = response.xpath('//a[@class="nxt"]')
        if len(next_btn) > 0:
            next_page_url = base_url + next_btn[0].xpath('./@href').extract()[0]
            self.log('next_page_url:' + next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        item = HeartbridgeItem()
        title = response.xpath('//a[@id="thread_subject"]/text()').extract()[0]
        self.log('title:' + title)
        url = response.url
        self.log('url:' + url)
        content = response.xpath('//td[@class="t_f"]/text()').extract()
        content = ''.join(content)
        self.log('content:' + content)
        author = response.xpath('//a[@class="xw1"]/text()').extract()[0]
        self.log('author:' + author)
        date = response.xpath('//div[@class="authi"]/em/text()').extract()[0]
        self.log('date:' + date)
        item['title'] = title

        item['url'] = url
        item['content'] = content
        item['author'] = author
        item['date'] = date
        yield item
