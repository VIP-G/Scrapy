# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from peopleSpider.items import PeoplespiderItem

'''
level 2:
案例：人民网分布式爬虫
http://politics.people.com.cn/GB/1024/index1.html
爬取新闻标题，链接，内容，发表时间
'''


class PpsSpider(RedisCrawlSpider):
    name = 'pps'
    # allowed_domains = ['people.com.cn']
    # start_urls = ['http://people.com.cn/']
    redis_key = 'pps:start_urls'

    link_page = LinkExtractor(restrict_xpaths=('//div[@class="page_n clearfix"]/a'))
    detail = LinkExtractor(restrict_xpaths=('//div[@class="ej_list_box clear"]/ul/li/a'))
    rules = [
        Rule(link_page, follow=True),
        Rule(detail, callback='parse_detail'),

    ]

    def parse_detail(self, response):
        '''
        提取新闻详情
        :param response:
        :return:
        '''
        title = response.xpath('//div[@class="clearfix w1000_320 text_title"]/h1/text()').extract()[0]
        url = response.url
        date = response.xpath('//div[@class="box01"]/div[1]/text()').extract()[0]
        date = date.strip().split(' ')[0]
        source = response.xpath('//div[@class="box01"]/div[1]/a/text()').extract()
        if len(source) > 0:
            source = source[0]
        else:
            source = '空'

        content = response.xpath('//div[@class="box_con"]//text()').extract()
        content = ''.join(content).strip()
        self.log('标题:' + title)
        self.log('链接:' + url)
        self.log('发表时间:' + date)
        self.log('来源:' + source)
        self.log('内容:' + content)
        self.log('*' * 200)

        item = PeoplespiderItem()
        item['title'] = title
        item['url'] = url
        item['date'] = date
        item['source'] = source
        item['content'] = content
        yield item
