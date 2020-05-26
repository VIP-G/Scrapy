from scrapy import cmdline

name = 'pythonJobSpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
