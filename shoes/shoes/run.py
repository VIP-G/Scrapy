from scrapy import cmdline

name='shoesimg'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())