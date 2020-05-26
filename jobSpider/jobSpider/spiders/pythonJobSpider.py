# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from jobSpider.items import JobspiderItem

class PythonjobspiderSpider(RedisCrawlSpider):
    name = 'pythonJobSpider'
    redis_key = 'pythonJobSpider:start_urls'
    # 链接的特征
    link_page = LinkExtractor(restrict_xpaths=('//li[@class="bk"]/a'))

    rules = [

        Rule(link_page, follow=True, callback='parse_content')
    ]

    def parse_content(self, response):

        # 提取招聘信息条目的列表
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')

        for each in job_list:
            name = each.xpath('./p/span/a/text()').extract()[0].strip()
            self.log('name:' + name)
            # 招聘公司
            corp = each.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
            self.log('corp:' + corp)
            # 工作地点
            city = each.xpath('./span[@class="t3"]/text()').extract()[0].strip()
            self.log('city:' + city)
            # 薪资待遇
            salary = each.xpath('./span[@class="t4"]/text()').extract()
            if len(salary) > 0:
                salary = salary[0].strip()
            else:
                salary = '面议'
            self.log('salary:' + salary)
            # 发布时间
            pub_date = each.xpath('./span[@class="t5"]/text()').extract()[0]
            self.log('pub_date:' + pub_date)
            item = JobspiderItem()
            item['name'] = name
            item['corp'] = corp
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date
            yield item
            self.log('*' * 200)
