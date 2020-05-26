from scrapy import cmdline

name='counrystat'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())