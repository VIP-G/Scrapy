# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import  Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from blogSpider.items import BlogspiderItem

'''

案例：sina 博客分布式爬虫
http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html
爬取博客标题，url,内容
'''



class BlogSpider(RedisCrawlSpider):
    name = 'blog'
    # allowed_domains = ['sina.com.cn']
    # start_urls = ['http://sina.com.cn/']
    redis_key = 'blog:start_urls'

    # 翻页链接提取器:描述筛选翻页链接的特征
    link_page = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    # 详情链接的提取器：描述筛选详情链接的特征
    link_item = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a'))
    rules = [
        Rule(link_page, follow=True),
        Rule(link_item, callback='parse_content')
    ]

    def parse_content(self, response):
        self.log('parse_content...')
        item = BlogspiderItem()
        title = response.xpath('//div[@class="articalTitle"]/h2/text()').extract()[0]
        self.log('title:' + title)
        url = response.url
        self.log('url:' + url)
        content = response.xpath('//div[@class="articalContent   newfont_family"]//text()').extract()
        content = ''.join(content)
        self.log(content)
        item['title'] = title
        item['url'] = url
        item['content'] = content

        yield item