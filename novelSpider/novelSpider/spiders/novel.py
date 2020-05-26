# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from novelSpider.items import NovelspiderItem
'''
全本小说（CrawlSpider）
https://www.quanben.net/list/2_1.html
爬取小说名称，url，类别，作者，更新时间，状态
'''

class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['quanben.net']
    start_urls = ['https://www.quanben.net/list/2_1.html']


    # 翻页链接提取器:描述筛选翻页链接的特征
    link_page = LinkExtractor(restrict_xpaths=(''))
    # 详情链接的提取器：描述筛选详情链接的特征
    link_item = LinkExtractor(restrict_xpaths=(''))
    rules = [
        Rule(link_page, follow=True),
        Rule(link_item, callback='parse_content')
    ]
