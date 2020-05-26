# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from heartBridge.items import HeartbridgeItem


class T2Spider(CrawlSpider):
    name = 't3'
    allowed_domains = ['zynews.cn']
    start_urls = ['https://xtq.zynews.cn/wzpostlist.php?mod=list']

    # 翻页链接提取器:描述筛选翻页链接的特征
    # link_page = LinkExtractor(restrict_xpaths=('//a[@class="nxt"]'))
    # link_page = LinkExtractor(restrict_css=('a.nxt'))
    link_page = LinkExtractor(allow=(r'wzpostlist\.php\?mod=list'))
    # 详情链接的提取器：描述筛选详情链接的特征
    # link_item = LinkExtractor(restrict_xpaths=('//th[@class="new"]/a'))
    # link_item = LinkExtractor(restrict_css=('th.new > a'))
    link_item = LinkExtractor(allow=('thread.*?\.html'))
    rules = [
        Rule(link_page, follow=True),
        Rule(link_item, callback='parse_content')
    ]

    def parse_content(self, response):
        self.log('parse_content...')
        item = HeartbridgeItem()
        title = response.xpath('//a[@id="thread_subject"]/text()').extract()[0]
        self.log('title:' + title)
        url = response.url
        content = response.xpath('//td[@class="t_f"]/text()').extract()
        content = ''.join(content)
        self.log('content:' + content)
        author = response.xpath('//a[@class="xw1"]/text()').extract()[0]
        self.log('author:' + author)
        date = response.xpath('//div[@class="pti"]/div[@class="authi"]/em/text()').extract()[0]
        date = date[3:].strip()
        self.log('date:' + date)
        item['title'] = title
        item['url'] = url
        item['content'] = content
        item['author'] = author
        item['date'] = date
        yield item
