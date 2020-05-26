from scrapy import cmdline

name='image'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())