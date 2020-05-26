from scrapy import cmdline

name = 'game'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

# lpush game:start_urls http://search.97973.com/guides/search?search_key=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8
