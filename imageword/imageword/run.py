from scrapy import cmdline

name='imgword'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())