from scrapy import cmdline

name = 'blog'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

# lpush blog:start_urls http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html

