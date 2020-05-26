# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from westGame.items import WestgameItem

'''
大话西游攻略分布式爬虫
http://search.97973.com/guides/search?search_key=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8
爬取标题，日期，来源，攻略内容
'''


class GameSpider(RedisCrawlSpider):
    name = 'game'
    # allowed_domains = ['97973.com']
    #     # start_urls = ['http://97973.com/']
    redis_key = 'game:start_urls'

    link_page = LinkExtractor(restrict_xpaths=('//div[@class="ListPage"]/span/a'))
    deatil = LinkExtractor(restrict_xpaths=('//div[@class="hot_wrap"]/ul/li/a'))
    rules = [
        Rule(link_page, follow=True),
        Rule(deatil, callback='parse_detail'),
    ]

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="F-yahei"]/text()').extract()[0]
        self.log('title:' + title)
        date = response.xpath('//div[@class="lightgray F-song txtdetail"]/text()').extract()[1]
        date = date.strip().split(' ')[0]
        self.log('date:' + date)
        source = response.xpath('//div[@class="lightgray F-song txtdetail"]/a/text()').extract()[0]
        self.log('source:' + source)
        body = response.xpath('//div[@id="fonttext"]//text()').extract()
        body = ''.join(body).strip()
        self.log(body)
        item = WestgameItem()
        item['title'] = title
        item['date'] = date
        item['source'] = source
        item['body'] = body
        yield item
