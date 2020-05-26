# -*- coding: utf-8 -*-
import scrapy
import time
from economic21.items import Economic21Item


class Eco21Spider(scrapy.Spider):
    name = 'eco21'
    allowed_domains = ['www.21jingji.com']
    start_urls = ['http://www.21jingji.com/channel/finance/']

    curent_page = 1
    time = int(time.time())
    base_url = 'http://www.21jingji.com/channel/finance/{}.html'
    has_next = True

    def parse(self, response):
        ls = response.xpath('//div[@id="data_list"]/div/a[@class="listImg"]')
        self.log('len:' + str(len(ls)))
        for i in ls:
            detail_url = i.xpath('./@href').extract()[0]
            self.log('详情连接:' + detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)
        self.curent_page += 1
        next = response.xpath('//p[@class="moreP"]/a/text()').extract()[0]

        if next == '查看更多':
            next_url = 'http://www.21jingji.com/channel/finance/{}.html?'.format(self.curent_page)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, res):
        item = Economic21Item()
        title = res.xpath('//h2[@class="titl"]/text()').extract()[0]
        self.log('标题:' + title)
        day = res.xpath('//p[@class="Wh"]/span[1]/text()').extract()[0]
        tm = res.xpath('//p[@class="Wh"]/span[2]/text()').extract()[0]
        date = day + tm
        self.log('发布时间:' + date)
        s1 = res.xpath('//p[@class="Wh"]/span[3]/text()').extract()[0]
        s2 = res.xpath('//p[@class="Wh"]/span[4]/text()').extract()[0]
        source = s1 + s2
        self.log('来源:' + source)
        content = res.xpath('//div[@class="detailCont"]//text()').extract()[0:-4]
        content = ''.join(content).strip()
        self.log('内容:' + content)
        item['title'] = title
        item['date'] = date
        item['source'] = source
        item['content'] = content
        yield item
