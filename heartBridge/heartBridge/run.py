from scrapy import cmdline

name = 'heartB3'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

# lpush heartB2:start_urls https://xtq.zynews.cn/wzpostlist.php?mod=list
# lpush heartB3:start_urls https://xtq.zynews.cn/wzpostlist.php?mod=list
