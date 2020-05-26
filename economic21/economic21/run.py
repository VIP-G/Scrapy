from scrapy import cmdline

name='eco21'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())