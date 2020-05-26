# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountrystatisItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    next_url = scrapy.Field()
    detail_url = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()


