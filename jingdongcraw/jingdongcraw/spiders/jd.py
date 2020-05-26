# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from jingdongcraw.items import JingdongcrawItem


class JdSpider(RedisCrawlSpider):
    name = 'jd'
    redis_key = 'jd:start_urls'

    link_page = LinkExtractor(restrict_xpaths=('//map[@id="Map_m"]/area'))
    link_good = LinkExtractor(restrict_xpaths=('//ul[@class="gl-warp clearfix"]/div[@class="p-img"]/a'))

    rules = [
        Rule(link_page, follow=True),
        # Rule(link_good, callback='parse_detail')
    ]


    def parse_detail(self, res):
        self.log(8888)
